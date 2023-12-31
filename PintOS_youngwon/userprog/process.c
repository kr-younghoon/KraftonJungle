#include "userprog/process.h"
#include <debug.h>
#include <inttypes.h>
#include <round.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "userprog/gdt.h"
#include "userprog/tss.h"
#include "filesys/directory.h"
#include "filesys/file.h"
#include "filesys/filesys.h"
#include "threads/flags.h"
#include "threads/init.h"
#include "threads/interrupt.h"
#include "threads/palloc.h"
#include "threads/thread.h"
#include "threads/mmu.h"
#include "threads/vaddr.h"
#include "intrinsic.h"
#include "userprog/syscall.h"
#define VM
#ifdef VM
#include "vm/vm.h"
#endif

#include "filesys/file.h"

static void process_cleanup(void);
static bool load(const char *file_name, struct intr_frame *if_);
static void initd(void *f_name);
static void __do_fork(void *);

/* General process initializer for initd and other process. */
static void
process_init(void)
{
	struct thread *current = thread_current();
	// printf("process_init IN/OUT - process.c:37\n");
}

/* Starts the first userland program, called "initd", loaded from FILE_NAME.
 * The new thread may be scheduled (and may even exit)
 * before process_create_initd() returns. Returns the initd's
 * thread id, or TID_ERROR if the thread cannot be created.
 * Notice that THIS SHOULD BE CALLED ONCE. */
tid_t process_create_initd(const char *file_name)
{
	char *fn_copy, *save_ptr;
	tid_t tid;

	/* Make a copy of FILE_NAME.
	 * Otherwise there's a race between the caller and load(). */
	fn_copy = palloc_get_page(0); // 커널 모드에 할당
	if (fn_copy == NULL)
		return TID_ERROR;
	strlcpy(fn_copy, file_name, PGSIZE);

	// 입력받은 명령어 중에서 가장 앞의 토큰 = 스레드 이름
	strtok_r(file_name, " ", &save_ptr);

	/* Create a new thread to execute FILE_NAME. */
	tid = thread_create(file_name, PRI_DEFAULT, initd, fn_copy);
	if (tid == TID_ERROR)
		palloc_free_page(fn_copy);
	return tid;
}

/* A thread function that launches first user process. */
static void
initd(void *f_name)
{
	// printf("안녕하세요!\n");
#ifdef VM
	// printf("#ifdef VM -> supplemental_page_table_init process.c:72\n");
	supplemental_page_table_init(&thread_current()->spt);
	// printf("#ifdef end spt초기화완료 - process.c:74\n");
#endif
	// printf("#endif process_init(); process.c:77\n");
	process_init();
	// printf("process_init() -> if(process_exec()<0) process.c:79\n");
	if (process_exec(f_name) < 0) {
		// printf("PANIC FAIL TO LAUNCH INITD : process.c:81\n");
		PANIC("Fail to launch initd\n");
	}
	// printf("NOT_REACHED();\n");
	NOT_REACHED();
}

/* Clones the current process as `name`. Returns the new process's thread id, or
 * TID_ERROR if the thread cannot be created. */
tid_t process_fork(const char *name, struct intr_frame *if_ UNUSED)
{
	/* Clone current thread to new thread.*/
	struct thread *curr = thread_current();
	memcpy(&curr->parent_if, if_, sizeof(struct intr_frame));

	tid_t tid = thread_create(name, PRI_DEFAULT, __do_fork, curr);
	if (tid == TID_ERROR)
	{
		return TID_ERROR;
	}

	struct thread *child = get_child_process(tid);
	sema_down(&child->load_sema);
	if (child->exit_status == -2)
	{
		// sema_up(&child->exit_sema);
		return TID_ERROR;
	}

	return tid;
}

#ifndef VM
/* Duplicate the parent's address space by passing this function to the
 * pml4_for_each. This is only for the project 2. */
static bool
duplicate_pte(uint64_t *pte, void *va, void *aux)
{
	struct thread *current = thread_current();
	struct thread *parent = (struct thread *)aux;
	void *parent_page;
	void *newpage;
	bool writable;

	/* 1. TODO: If the parent_page is kernel page, then return immediately. */
	if (is_kernel_vaddr(va))
	{
		return true;
	}

	/* 2. Resolve VA from the parent's page map level 4. */
	parent_page = pml4_get_page(parent->pml4, va);
	if (parent_page == NULL)
	{
		return false;
	}

	/* 3. TODO: Allocate new PAL_USER page for the child and set result to
	 *    TODO: NEWPAGE. */
	newpage = palloc_get_page(PAL_USER | PAL_ZERO);
	if (newpage == NULL)
	{
		return false;
	}

	/* 4. TODO: Duplicate parent's page to the new page and
	 *    TODO: check whether parent's page is writable or not (set WRITABLE
	 *    TODO: according to the result). */
	memcpy(newpage, parent_page, PGSIZE);
	writable = is_writable(pte);

	/* 5. Add new page to child's page table at address VA with WRITABLE
	 *    permission. */
	if (!pml4_set_page(current->pml4, va, newpage, writable))
	{
		/* 6. TODO: if fail to insert page, do error handling. */
		return false;
	}
	return true;
}
#endif

/* A thread function that copies parent's execution context.
 * Hint) parent->tf does not hold the userland context of the process.
 *       That is, you are required to pass second argument of process_fork to
 *       this function. */
static void
__do_fork(void *aux)
{
	struct intr_frame if_;
	struct thread *parent = (struct thread *)aux;
	struct thread *current = thread_current();
	/* TODO: somehow pass the parent_if. (i.e. process_fork()'s if_) */
	struct intr_frame *parent_if = &parent->parent_if;
	bool succ = true;

	/* 1. Read the cpu context to local stack. */
	memcpy(&if_, parent_if, sizeof(struct intr_frame));
	if_.R.rax = 0; // 자식 프로세스의 리턴값 0으로 설정

	/* 2. Duplicate PT */
	current->pml4 = pml4_create();
	if (current->pml4 == NULL)
		goto error;

	process_activate(current);
#ifdef VM
	supplemental_page_table_init(&current->spt);
	if (!supplemental_page_table_copy(&current->spt, &parent->spt))
		goto error;
#else
	if (!pml4_for_each(parent->pml4, duplicate_pte, parent))
		goto error;
#endif

	/* TODO: Your code goes here.
	 * TODO: Hint) To duplicate the file object, use `file_duplicate`
	 * TODO:       in include/filesys/file.h. Note that parent should not return
	 * TODO:       from the fork() until this function successfully duplicates
	 * TODO:       the resources of parent.*/

	// FDT 복사
	for (int i = 0; i < FDT_COUNT_LIMIT; i++)
	{
		struct file *file = parent->fdt[i];
		if (file == NULL)
		{
			continue;
		}
		if (file > 2)
		{
			file = file_duplicate(file);
		}
		current->fdt[i] = file;
	}
	current->next_fd = parent->next_fd;
	sema_up(&current->load_sema);
	process_init();
	/* Finally, switch to the newly created process. */
	if (succ)
		do_iret(&if_);
error:
	sema_up(&current->load_sema);
	// thread_exit();
	exit(-2);
}

/* Switch the current execution context to the f_name.
 * Returns -1 on fail. */
int process_exec(void *f_name)
{
	char *file_name = f_name;
	bool success;

	// printf("process exec start - process.c:235\n");

	/* We cannot use the intr_frame in the thread structure.
	 * This is because when current thread rescheduled,
	 * it stores the execution information to the member. */
	struct intr_frame _if;
	_if.ds = _if.es = _if.ss = SEL_UDSEG;
	_if.cs = SEL_UCSEG;
	_if.eflags = FLAG_IF | FLAG_MBS;

	/* We first kill the current context */
	process_cleanup();
	// printf("process_cleanup() - process.c:247\n");
	/* ---------------추가한 부분------------- */
	// parsing
	char *save_ptr, *tocken;
	char *arg[64];
	int count = 0;
	for (tocken = strtok_r(file_name, " ", &save_ptr); tocken != NULL; tocken = strtok_r(NULL, " ", &save_ptr))
	{
		arg[count] = tocken;
		count++;
	}
	/* ---------------------------------- */
	// printf("succ = load() process.c:259\n");
	/* And then load the binary */
	lock_acquire(&filesys_lock);
	success = load(file_name, &_if);
	lock_release(&filesys_lock);
	// printf("process.c:262\n");
	if (!success)
	{
		// printf("if(!success) - process.c:265\n");
		palloc_free_page(file_name);
		return -1;
	}
	// printf("process.c:269\n");
	/* ---------------추가한 부분------------- */
	// set up stack
	argument_stack(arg, count, &_if.rsp);
	_if.R.rdi = count;				 // argc 값 저장
	_if.R.rsi = (char *)_if.rsp + 8; // argv의 시작 주소 저장

	// hex_dump(_if.rsp, _if.rsp, USER_STACK - (uint64_t)_if.rsp, true);
	/* ---------------------------------- */
	// printf("process.c:274\n");
	/* If load failed, quit. */
	palloc_free_page(file_name);
	// if (!success)
	// 	return -1;
	/* Start switched process. */
	// printf("process.c:280\n");
	// printf("%d\n",&_if);
	do_iret(&_if);
	// printf("process.c:282\n");
	NOT_REACHED();
	// printf("end - process.c:279\n");
}

/* Waits for thread TID to die and returns its exit status.  If
 * it was terminated by the kernel (i.e. killed due to an
 * exception), returns -1.  If TID is invalid or if it was not a
 * child of the calling process, or if process_wait() has already
 * been successfully called for the given TID, returns -1
 * immediately, without waiting.
 *
 * This function will be implemented in problem 2-2.  For now, it
 * does nothing. */
int process_wait(tid_t child_tid UNUSED)
{
	/* XXX: Hint) The pintos exit if process_wait (initd), we recommend you
	 * XXX:       to add infinite loop here before
	 * XXX:       implementing the process_wait. */
	struct thread *child = get_child_process(child_tid);
	// printf("[process_wait] run \t\t\t\t| process.c:307\n");
	if (child == NULL)
	{
		// printf("[process_wait]if(child == NULL) t\t\t| process.c:315\n");
		return -1;
	}
	sema_down(&child->wait_sema);
	list_remove(&child->child_elem);
	sema_up(&child->exit_sema);
	// printf("[process_wait] stop \t\t\t\t| process.c:315\n");
	return child->exit_status;
}

/* Exit the process. This function is called by thread_exit (). */
void process_exit(void)
{
	struct thread *curr = thread_current();
	/* TODO: Your code goes here.
	 * TODO: Implement process termination message (see
	 * TODO: project2/process_termination.html).
	 * TODO: We recommend you to implement process resource cleanup here. */

	// FDT 메모리 해제하기
	for (int i = 2; i < FDT_COUNT_LIMIT; i++)
	{
		close(i);
	}
	palloc_free_page(curr->fdt);
	file_close(curr->running);
	process_cleanup();
	sema_up(&curr->wait_sema);
	sema_down(&curr->exit_sema);
}

/* Free the current process's resources. */
static void
process_cleanup(void)
{
	struct thread *curr = thread_current();

#ifdef VM
	supplemental_page_table_kill(&curr->spt);
#endif

	uint64_t *pml4;
	/* Destroy the current process's page directory and switch back
	 * to the kernel-only page directory. */
	pml4 = curr->pml4;
	if (pml4 != NULL)
	{
		/* Correct ordering here is crucial.  We must set
		 * cur->pagedir to NULL before switching page directories,
		 * so that a timer interrupt can't switch back to the
		 * process page directory.  We must activate the base page
		 * directory before destroying the process's page
		 * directory, or our active page directory will be one
		 * that's been freed (and cleared). */
		curr->pml4 = NULL;
		pml4_activate(NULL);
		pml4_destroy(pml4);
	}
}

/* Sets up the CPU for running user code in the nest thread.
 * This function is called on every context switch. */
void process_activate(struct thread *next)
{
	/* Activate thread's page tables. */
	pml4_activate(next->pml4);

	/* Set thread's kernel stack for use in processing interrupts. */
	tss_update(next);
}

/* We load ELF binaries.  The following definitions are taken
 * from the ELF specification, [ELF1], more-or-less verbatim.  */

/* ELF types.  See [ELF1] 1-2. */
#define EI_NIDENT 16

#define PT_NULL 0			/* Ignore. */
#define PT_LOAD 1			/* Loadable segment. */
#define PT_DYNAMIC 2		/* Dynamic linking info. */
#define PT_INTERP 3			/* Name of dynamic loader. */
#define PT_NOTE 4			/* Auxiliary info. */
#define PT_SHLIB 5			/* Reserved. */
#define PT_PHDR 6			/* Program header table. */
#define PT_STACK 0x6474e551 /* Stack segment. */

#define PF_X 1 /* Executable. */
#define PF_W 2 /* Writable. */
#define PF_R 4 /* Readable. */

/* Executable header.  See [ELF1] 1-4 to 1-8.
 * This appears at the very beginning of an ELF binary. */
struct ELF64_hdr
{
	unsigned char e_ident[EI_NIDENT];
	uint16_t e_type;
	uint16_t e_machine;
	uint32_t e_version;
	uint64_t e_entry;
	uint64_t e_phoff;
	uint64_t e_shoff;
	uint32_t e_flags;
	uint16_t e_ehsize;
	uint16_t e_phentsize;
	uint16_t e_phnum;
	uint16_t e_shentsize;
	uint16_t e_shnum;
	uint16_t e_shstrndx;
};

struct ELF64_PHDR
{
	uint32_t p_type;
	uint32_t p_flags;
	uint64_t p_offset;
	uint64_t p_vaddr;
	uint64_t p_paddr;
	uint64_t p_filesz;
	uint64_t p_memsz;
	uint64_t p_align;
};

/* Abbreviations */
#define ELF ELF64_hdr
#define Phdr ELF64_PHDR

static bool setup_stack(struct intr_frame *if_);
static bool validate_segment(const struct Phdr *, struct file *);
static bool load_segment(struct file *file, off_t ofs, uint8_t *upage,
						 uint32_t read_bytes, uint32_t zero_bytes,
						 bool writable);

/* Loads an ELF executable from FILE_NAME into the current thread.
 * Stores the executable's entry point into *RIP
 * and its initial stack pointer into *RSP.
 * Returns true if successful, false otherwise. */
static bool
load(const char *file_name, struct intr_frame *if_)
{
	struct thread *t = thread_current();
	struct ELF ehdr;
	struct file *file = NULL;
	off_t file_ofs;
	bool success = false;
	int i;
	// printf("load 시작 : process.c:453\n");
	/* Allocate and activate page directory. */
	t->pml4 = pml4_create();
	if (t->pml4 == NULL)
		goto done;
	process_activate(thread_current());

	/* Open executable file. */
	file = filesys_open(file_name);
	if (file == NULL)
	{
		printf("load: %s: open failed\n", file_name);
		goto done;
	}

	/* Read and verify executable header. */
	if (file_read(file, &ehdr, sizeof ehdr) != sizeof ehdr || memcmp(ehdr.e_ident, "\177ELF\2\1\1", 7) || ehdr.e_type != 2 || ehdr.e_machine != 0x3E // amd64
		|| ehdr.e_version != 1 || ehdr.e_phentsize != sizeof(struct Phdr) || ehdr.e_phnum > 1024)
	{
		printf("load: %s: error loading executable\n", file_name);
		goto done;
	}

	/* Read program headers. */
	file_ofs = ehdr.e_phoff;
	for (i = 0; i < ehdr.e_phnum; i++)
	{
		struct Phdr phdr;
		// printf("load-for문 loop // process.c:481\n");
		if (file_ofs < 0 || file_ofs > file_length(file))
			goto done;
		file_seek(file, file_ofs);

		if (file_read(file, &phdr, sizeof phdr) != sizeof phdr)
			goto done;
		file_ofs += sizeof phdr;
		switch (phdr.p_type)
		{
		case PT_NULL:
		case PT_NOTE:
		case PT_PHDR:
		case PT_STACK:
		default:
			/* Ignore this segment. */
			break;
		case PT_DYNAMIC:
		case PT_INTERP:
		case PT_SHLIB:
			goto done;
		case PT_LOAD:
			if (validate_segment(&phdr, file))
			{
				bool writable = (phdr.p_flags & PF_W) != 0;
				uint64_t file_page = phdr.p_offset & ~PGMASK;
				uint64_t mem_page = phdr.p_vaddr & ~PGMASK;
				uint64_t page_offset = phdr.p_vaddr & PGMASK;
				uint32_t read_bytes, zero_bytes;
				if (phdr.p_filesz > 0)
				{
					/* Normal segment.
					 * Read initial part from disk and zero the rest. */
					read_bytes = page_offset + phdr.p_filesz;
					zero_bytes = (ROUND_UP(page_offset + phdr.p_memsz, PGSIZE) - read_bytes);
					// printf("if : process.c:516\n");
				}
				else
				{
					/* Entirely zero.
					 * Don't read anything from disk. */
					read_bytes = 0;
					zero_bytes = ROUND_UP(page_offset + phdr.p_memsz, PGSIZE);
					// printf("else : process.c:523\n");
				}
				// printf("load-load_seg-run // process.c:526\n");
				if (!load_segment(file, file_page, (void *)mem_page,
								  read_bytes, zero_bytes, writable)) {
					// printf("if !load_seg : process.c:528\n");
					goto done;
				}
			}
			else {
				goto done;
				// printf("else goto done; : process.c:534\n");
			}
			break;
		}
	}

	t->running = file;
	file_deny_write(file);
	// printf("load-setup_stack()-run // process.c:543\n");
	/* Set up stack. */
	if (!setup_stack(if_)) {
		goto done;
		// printf("load-setup_stack()-in/out // process.c:548\n");
	}
	/* Start address. */
	if_->rip = ehdr.e_entry;

	/* TODO: Your code goes here.
	 * TODO: Implement argument passing (see project2/argument_passing.html). */

	success = true;

done:
	/* We arrive here whether the load is successful or not. */
	// file_close (file);
	return success;
}

/* Checks whether PHDR describes a valid, loadable segment in
 * FILE and returns true if so, false otherwise. */
static bool
validate_segment(const struct Phdr *phdr, struct file *file)
{
	/* p_offset and p_vaddr must have the same page offset. */
	if ((phdr->p_offset & PGMASK) != (phdr->p_vaddr & PGMASK))
		return false;

	/* p_offset must point within FILE. */
	if (phdr->p_offset > (uint64_t)file_length(file))
		return false;

	/* p_memsz must be at least as big as p_filesz. */
	if (phdr->p_memsz < phdr->p_filesz)
		return false;

	/* The segment must not be empty. */
	if (phdr->p_memsz == 0)
		return false;

	/* The virtual memory region must both start and end within the
	   user address space range. */
	if (!is_user_vaddr((void *)phdr->p_vaddr))
		return false;
	if (!is_user_vaddr((void *)(phdr->p_vaddr + phdr->p_memsz)))
		return false;

	/* The region cannot "wrap around" across the kernel virtual
	   address space. */
	if (phdr->p_vaddr + phdr->p_memsz < phdr->p_vaddr)
		return false;

	/* Disallow mapping page 0.
	   Not only is it a bad idea to map page 0, but if we allowed
	   it then user code that passed a null pointer to system calls
	   could quite likely panic the kernel by way of null pointer
	   assertions in memcpy(), etc. */
	if (phdr->p_vaddr < PGSIZE)
		return false;

	/* It's okay. */
	return true;
}

#ifndef VM
/* Codes of this block will be ONLY USED DURING project 2.
 * If you want to implement the function for whole project 2, implement it
 * outside of #ifndef macro. */

/* load() helpers. */
static bool install_page(void *upage, void *kpage, bool writable);

/* Loads a segment starting at offset OFS in FILE at address
 * UPAGE.  In total, READ_BYTES + ZERO_BYTES bytes of virtual
 * memory are initialized, as follows:
 *
 * - READ_BYTES bytes at UPAGE must be read from FILE
 * starting at offset OFS.
 *
 * - ZERO_BYTES bytes at UPAGE + READ_BYTES must be zeroed.
 *
 * The pages initialized by this function must be writable by the
 * user process if WRITABLE is true, read-only otherwise.
 *
 * Return true if successful, false if a memory allocation error
 * or disk read error occurs.
*/
static bool
load_segment(struct file *file, off_t ofs, uint8_t *upage,
			 uint32_t read_bytes, uint32_t zero_bytes, bool writable)
{
	ASSERT((read_bytes + zero_bytes) % PGSIZE == 0);
	ASSERT(pg_ofs(upage) == 0);
	ASSERT(ofs % PGSIZE == 0);

	file_seek(file, ofs);
	while (read_bytes > 0 || zero_bytes > 0)
	{
		/* Do calculate how to fill this page.
		 * We will read PAGE_READ_BYTES bytes from FILE
		 * and zero the final PAGE_ZERO_BYTES bytes. */
		size_t page_read_bytes = read_bytes < PGSIZE ? read_bytes : PGSIZE;
		size_t page_zero_bytes = PGSIZE - page_read_bytes;

		/* Get a page of memory. */
		uint8_t *kpage = palloc_get_page(PAL_USER);
		if (kpage == NULL)
			return false;

		/* Load this page. */
		if (file_read(file, kpage, page_read_bytes) != (int)page_read_bytes)
		{
			palloc_free_page(kpage);
			return false;
		}
		memset(kpage + page_read_bytes, 0, page_zero_bytes);

		/* Add the page to the process's address space. */
		if (!install_page(upage, kpage, writable))
		{
			printf("fail\n");
			palloc_free_page(kpage);
			return false;
		}

		/* Advance. */
		read_bytes -= page_read_bytes;
		zero_bytes -= page_zero_bytes;
		upage += PGSIZE;
	}
	return true;
}

/* Create a minimal stack by mapping a zeroed page at the USER_STACK */
static bool
setup_stack(struct intr_frame *if_)
{
	uint8_t *kpage;
	bool success = false;

	kpage = palloc_get_page(PAL_USER | PAL_ZERO);
	if (kpage != NULL)
	{
		success = install_page(((uint8_t *)USER_STACK) - PGSIZE, kpage, true);
		if (success)
			if_->rsp = USER_STACK;
		else
			palloc_free_page(kpage);
	}
	return success;
}

/* Adds a mapping from user virtual address UPAGE to kernel
 * virtual address KPAGE to the page table.
 * If WRITABLE is true, the user process may modify the page;
 * otherwise, it is read-only.
 * UPAGE must not already be mapped.
 * KPAGE should probably be a page obtained from the user pool
 * with palloc_get_page().
 * Returns true on success, false if UPAGE is already mapped or
 * if memory allocation fails. */
static bool
install_page(void *upage, void *kpage, bool writable)
{
	struct thread *t = thread_current();

	/* Verify that there's not already a page at that virtual
	 * address, then map our page there. */
	return (pml4_get_page(t->pml4, upage) == NULL && pml4_set_page(t->pml4, upage, kpage, writable));
}
#else
/* From here, codes will be used after project 3.
 * If you want to implement the function for only project 2, implement it on the
 * upper block. */

static bool
lazy_load_segment(struct page *page, void *aux)
{
	// printf("lazy_load_seg in - process.c:709\n");
	/* TODO: Load the segment from the file */
	/* TODO: This called when the first page fault occurs on address VA. */
	/* TODO: VA is available when calling this function. */
	struct lazy_load_arg *lazy_load_arg = (struct lazy_load_arg *)aux;

	// 1) 파일의 position을 ofs으로 지정한다.
	file_seek(lazy_load_arg->file, lazy_load_arg->ofs);
	// 2) 파일을 read_bytes만큼 물리 프레임에 읽어 들인다.
	if (file_read(lazy_load_arg->file, page->frame->kva, lazy_load_arg->read_bytes) != (int)(lazy_load_arg->read_bytes)) {
		palloc_free_page(page->frame->kva);
		// printf("lazy_load_seg false return - process.c:720\n");
		return false;
	}
	// 3) 다 읽은 지점부터 zero_bytes만큼 0으로 채운다.
	memset(page->frame->kva + lazy_load_arg->read_bytes, 0, lazy_load_arg->zero_bytes);
	// printf("lazy_load_seg true return - process.c:725\n");
	return true;
}



/* (수정, 10) 이 함수는 프로세스가 실행될 때, 실행 파일을 현재 스레드로 로드하는 함수인 load함수에서 호출된다.
	-> 파일 내용을 upage에 로드하는 함수이다. 파일의 내용을 로드하기 위해서 upage를 할당할 page가 필요한데,
	위에서 수정한 vm_alloc_page_with_initializer 함수를 호출해서 페이지를 생성한다.

	Lazy Loading 을 사용해야 하므로, 여기서 바로 파일의 내용을 로드하지 않아야 한다.
	그래서 page에 내용을 로드할 때 사용할 함수와 필요한 인자들을 넣어줘야 하는데,
	vm_alloc_page_with_initializer 함수의 네 번째, 다섯 번째 인자가 각각 로드할 때
	사용할 함수, 그리고 그 때 필요한 인자에 해당한다.

	내용을 로드할 때 사용할 함수는 Lazy_load_segment를 사용하고, 인자는 직접 만들어서 넘겨줘야 한다.
	lazy_load_segment에서 필요한 정보는 아래와 같다.
	 - `file`          : 내용이 담긴 파일 객체
	 - `ofs`           : 이 페이지에서 읽기 시작할 위치
	 - `read_bytes`    : 이 페이지에서 읽어야 하는 바이트의 수
	 - `zero_bytes`    : 이 페이지에서 read_bytes만큼 읽고 공간이 남아 0으로 채워야 하는 바이트 수
	 - `lazy_load_arg` : 라는 구조체를 새로 정의해서 선언하고 안에 위 정보들을 담아서 vm_alloc_page_with_initializer 함수의 마지막 인자로 전달했다
	
	이제 page fault가 처음 발생했을 때, lazy_load_segment가 실행되고, lazy_load_arg가 인자로 사용되어 내용이 로딩될 것이다. */
static bool
load_segment(struct file *file, off_t ofs, uint8_t *upage,
			 uint32_t read_bytes, uint32_t zero_bytes, bool writable)
{
	// printf("load_seg(start) - process.c:764\n");
	ASSERT((read_bytes + zero_bytes) % PGSIZE == 0);
	ASSERT(pg_ofs(upage) == 0);
	ASSERT(ofs % PGSIZE == 0);
	// printf("load_seg(assert) - process.c:768\n");
	while (read_bytes > 0 || zero_bytes > 0)
	{
		// printf("while running - process.c:771\n");
		/* Do calculate how to fill this page.
		 * We will read PAGE_READ_BYTES bytes from FILE
		 * and zero the final PAGE_ZERO_BYTES bytes. */
		size_t page_read_bytes = read_bytes < PGSIZE ? read_bytes : PGSIZE;
		size_t page_zero_bytes = PGSIZE - page_read_bytes;

		/* TODO: Set up aux to pass information to the lazy_load_segment. */
		struct lazy_load_arg *lazy_load_arg = (struct lazy_load_arg *)malloc(sizeof(struct lazy_load_arg));
		lazy_load_arg->file = file;
		lazy_load_arg->ofs = ofs;
		lazy_load_arg->read_bytes = page_read_bytes;
		lazy_load_arg->zero_bytes = page_zero_bytes;
		if (!vm_alloc_page_with_initializer(VM_ANON, upage,
											writable, lazy_load_segment, lazy_load_arg)) {
			// printf("load_seg(vp_init) -> false - process.c:786\n");
			return false;
		}

		/* Advance. */
		read_bytes -= page_read_bytes;
 		zero_bytes -= page_zero_bytes;
		ofs += page_read_bytes;
		upage += PGSIZE;
		// printf("load_seg(Advance) -> true - process.c:781\n");
	}
	// printf("load_seg true return - process.c:785\n");
	return true;
}


/* Create a PAGE of stack at the USER_STACK. Return true on success. */
static bool
setup_stack(struct intr_frame *if_)
{
	// printf("setup_stack - process.c:799\n");
	bool success = false;
	// 스택은 아래로 성장하므로, USER_STACK에서 PGSIZE만큼 아래로 내린 지점에서 페이지를 생성한다.
	void *stack_bottom = (void *)(((uint8_t *)USER_STACK) - PGSIZE);
    // uint8_t kpage = palloc_get_page(PAL_USER | PAL_ZERO);

	/* TODO: Map the stack on stack_bottom and claim the page immediately.
	 * TODO: If success, set the rsp accordingly.
	 * TODO: You should mark the page is stack. */
	/* TODO: Your code goes here */
	// 스택을 stack_bottom에 매핑하고 즉시 페이지를 할당합니다. 
	// 성공하면 rsp를 적절히 설정합니다. 페이지를 스택으로 표시해야 합니다.
	// printf("--if.vm_alloc_page-- process.c:810\n");
	if(vm_alloc_page(VM_ANON | VM_MARKER_0, stack_bottom, 1)) {// (type, upage, writable)
		success = vm_claim_page(stack_bottom);
		// success = install_page(((uint8_t *)USER_STACK) - PGSIZE, kpage, true);
		if (success)
			if_ -> rsp = USER_STACK;
		// printf("%d\n", success);
		// printf("process.c:816\n");
	}
	// printf("setup_stack - process.c:820\n");
	return success;
}
#endif /* VM */

void argument_stack(char **argv, int argc, void **rsp)
{
	// command 오른쪽 단어부터 스택에 삽입
	for (int i = argc - 1; i >= 0; i--)
	{
		// 입력 받은 인자 1개 또한 스택에 넣어주는 것이므로 오른쪽 글자부터 넣어준다.
		for (int j = strlen(argv[i]); j >= 0; j--)
		{
			(*rsp)--;					 // 스택 주소 감소
			**(char **)rsp = argv[i][j]; // 주소에 문자 저장
		}
		argv[i] = *(char **)rsp; // 인자가 스택에 저장되어있는 주소를 배열에 저장
	}

	while ((int)(*rsp) % 8 != 0)
	{			  // 스택 포인터가 8의 배수가 되도록
		(*rsp)--; // 스택 포인터를 1바이트씩 이동
		**(uint8_t **)rsp = 0;
	}

	for (int i = argc; i >= 0; i--)
	{
		(*rsp) -= 8;
		if (i == argc) // argument의 끝을 나타내는 공백 추가
			**(char ***)rsp = 0;
		else // 각각의 argument가 스택에 저장되어있는 주소 저장
			**(char ***)rsp = argv[i];
	}

	(*rsp) -= 8; // return 값의 주소인 fake address 저장
	**(void ***)rsp = 0;
}

/*
 * 자식 리스트에서 child_tid를 가진 스레드 찾는 함수
 */
struct thread *get_child_process(tid_t child_tid)
{
	struct list *child = &thread_current()->child_list;
	for (struct list_elem *e = list_begin(child); e != list_end(child); e = list_next(e))
	{
		struct thread *t = list_entry(e, struct thread, child_elem);
		if (t->tid == child_tid)
		{
			return t;
		}
	}
	return NULL;
}

/*
 * 새로운 파일 객체제 대한 파일 디스크립터 생성하는 함수
 * fdt에도 추가해준다.
 */
int process_add_file(struct file *f)
{
	struct thread *cur = thread_current();
	struct file **fdt = cur->fdt;

	// 범위를 벗어나지 않고 인덱스에 값이 존재하지 않을 때까지
	while (cur->next_fd < FDT_COUNT_LIMIT && fdt[cur->next_fd])
	{
		cur->next_fd++;
	}

	if (cur->next_fd >= FDT_COUNT_LIMIT)
	{ // 범위를 넘어설 때까지 남은 공간이 없으면
		return -1;
	}
	fdt[cur->next_fd] = f;

	return cur->next_fd;
}

/*
 * FDT에서 fd값을 가진 파일 객체 제거
 */
void process_close_file(int fd)
{
	struct file **fdt = thread_current()->fdt;
	if (fd < 2 || fd >= FDT_COUNT_LIMIT)
	{
		return NULL;
	}
	fdt[fd] = NULL;
}

/*
 * fd가 가리키는 파일 반환하는 함수
 */
struct file *process_get_file(int fd)
{
	struct file **fdt = thread_current()->fdt;

	if (fd < 2 || fd >= FDT_COUNT_LIMIT)
	{
		return NULL;
	}
	return fdt[fd];
}