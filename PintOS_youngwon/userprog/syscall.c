#include "userprog/syscall.h"
#include <stdio.h>
#include <syscall-nr.h>
#include "threads/interrupt.h"
#include "threads/thread.h"
#include "threads/loader.h"
#include "userprog/gdt.h"
#include "threads/flags.h"
#include "intrinsic.h"

// 추가 헤더파일
#include "threads/synch.h"
#include "userprog/process.h"
#include "filesys/filesys.h"
#include "filesys/file.h"
#include "devices/input.h"
#include "threads/palloc.h"

void syscall_entry(void);
void syscall_handler(struct intr_frame *);

void check_address(void *addr);

// system call 대응 함수
void halt(void);
void exit(int status);
int fork(const char *thread_name, struct intr_frame *f);
int exec(const char *file);
int wait(int pid);
bool create(const char *file, unsigned initial_size);
bool remove(const char *file);
int open(const char *file);
int filesize(int fd);
int read(int fd, void *buffer, unsigned size);
int write(int fd, const void *buffer, unsigned size);
void seek(int fd, unsigned position);
unsigned tell(int fd);
void close(int fd);

void *mmap(void *addr, size_t length, int writable, int fd, off_t offset);

/* System call.
 *
 * Previously system call services was handled by the interrupt handler
 * (e.g. int 0x80 in linux). However, in x86-64, the manufacturer supplies
 * efficient path for requesting the system call, the `syscall` instruction.
 *
 * The syscall instruction works by reading the values from the the Model
 * Specific Register (MSR). For the details, see the manual. */

#define MSR_STAR 0xc0000081			/* Segment selector msr */
#define MSR_LSTAR 0xc0000082		/* Long mode SYSCALL target */
#define MSR_SYSCALL_MASK 0xc0000084 /* Mask for the eflags */

 // 파일 동기화를 위한 전역변수

void syscall_init(void) {
	write_msr(MSR_STAR, ((uint64_t)SEL_UCSEG - 0x10) << 48 |
							((uint64_t)SEL_KCSEG) << 32);
	write_msr(MSR_LSTAR, (uint64_t)syscall_entry);

	/* The interrupt service rountine should not serve any interrupts
	 * until the syscall_entry swaps the userland stack to the kernel
	 * mode stack. Therefore, we masked the FLAG_FL. */
	write_msr(MSR_SYSCALL_MASK,
			  FLAG_IF | FLAG_TF | FLAG_DF | FLAG_IOPL | FLAG_AC | FLAG_NT);

	lock_init(&filesys_lock); // lock 초기화
}

/* The main system call interface */
void syscall_handler(struct intr_frame *f UNUSED) {
	int sys_num = f->R.rax; // syscall number
#ifdef VM
	thread_current()->rsp = f->rsp; // 추가
#endif
	switch (sys_num) {
	case SYS_HALT:
		halt();
		break;
	case SYS_EXIT:
		exit(f->R.rdi);
		break;
	case SYS_FORK:
		f->R.rax = fork(f->R.rdi, f);
		break;
	case SYS_EXEC:
		f->R.rax = exec(f->R.rdi);
		break;
	case SYS_WAIT:
		f->R.rax = wait(f->R.rdi);
		break;
	case SYS_CREATE:
		f->R.rax = create(f->R.rdi, f->R.rsi);
		break;
	case SYS_REMOVE:
		f->R.rax = remove(f->R.rdi);
		break;
	case SYS_OPEN:
		f->R.rax = open(f->R.rdi);
		break;
	case SYS_FILESIZE:
		f->R.rax = filesize(f->R.rdi);
		break;
	case SYS_READ:
		f->R.rax = read(f->R.rdi, f->R.rsi, f->R.rdx);
		break;
	case SYS_WRITE:
		f->R.rax = write(f->R.rdi, f->R.rsi, f->R.rdx);
		break;
	case SYS_SEEK:
		seek(f->R.rdi, f->R.rsi);
		break;
	case SYS_TELL:
		f->R.rax = tell(f->R.rdi);
		break;
	case SYS_CLOSE:
		close(f->R.rdi);
	case SYS_MMAP:
		f->R.rax = mmap(f->R.rdi, f->R.rsi, f->R.rdx, f->R.r10, f->R.r8);
		break;
	case SYS_MUNMAP:
		munmap(f->R.rdi);
		break;
	}
}

/*
 * 주어진 주소가 올바른 주소인지 확인하는 함수
 */
void check_address(void *addr) {
	if (addr == NULL) {
		exit(-1); // 주소가 없을 경우
	}
	if (!is_user_vaddr(addr)) { // 유저 영역에 속해있지 않을 경우
		exit(-1);
	}
	// if(pml4_get_page(thread_current()->pml4, addr) == NULL) {
	// 	exit(-1);
	// }
}

// 운영체제를 중지한다.
void halt(void) {
	power_off(); // src/include/threads/init.h
}

// 현재 프로세스를 중지한다.
void exit(int status) {
	struct thread *curr = thread_current();
	curr->exit_status = status;
	printf("%s: exit(%d)\n", curr->name, status); // 종료 메시지 출력
	thread_exit();
}

// 현재 프로세스를 복사한다.
int fork(const char *thread_name, struct intr_frame *f) {
	return process_fork(thread_name, f);
}

// 현재 프로세스를 전환한다.
int exec(const char *file) {
	check_address(file);
	char *f_copy = palloc_get_page(0);
	if (f_copy == NULL) {
		exit(-1);
	}
	strlcpy(f_copy, file, PGSIZE);

	if (process_exec(f_copy) == -1) {
		exit(-1);
	}

	NOT_REACHED();
	return 0;
}

// 자식 프로세스가 끝날 떄까지 기다린다.
int wait(int pid) {
	// printf("[wait] \t\t\t\t| syscall.c:172\n");
	return process_wait(pid);
}

// 파일 생성
bool create(const char *file, unsigned initial_size) {
	lock_acquire(&filesys_lock);
	check_address(file); // 유저 영역의 주소인지 확인
	bool succ = filesys_create(file, initial_size);
	lock_release(&filesys_lock);
	return succ;
}

// 파일 삭제
bool remove(const char *file) {
	check_address(file); // 유저 영역의 주소인지 확인
	return filesys_remove(file);
}

// 파일 열기
int open(const char *file) {
	// printf("\n[open] start -> check_addr : \t\t\t| syscall.c:189\n");
	check_address(file);
	// printf("[open]check_addr -> lock_acq : %s \t\t| syscall.c:191\n", file);
	lock_acquire(&filesys_lock);
	struct file *f = filesys_open(file);
	// printf("[open]if f == NULL \t\t\t| syscall.c:194\n");
	if (f == NULL) {
		lock_release(&filesys_lock);

		// printf("f is null \t\t\t| syscall.c:196\n");
		return -1;
	}
	// printf("[open]file dscrptor \t\t\t| syscall.c:199\n");
	// 파일 디스크립터 생성하기 2
	int fd = process_add_file(f);
	// printf("[open]fd todjtd새엇ㅇ 이게 뭐야 ㅅㅂ \t\t\t| syscall.c:202\n");
	if (fd == -1) {
		file_close(f);
		// printf("open - file_close(f) \t\t\t| syscall.c:205\n");
	}
	lock_release(&filesys_lock);
	// printf("open out %d \t\t\t\t| syscall.c:207\n\n", fd);
	return fd;
}

// 파일 크기
int filesize(int fd) {
	struct file *f = process_get_file(fd); // fd를 이용해 파일 가져오기
	if (f == NULL) {
		return -1;
	}
	return file_length(f);
}

// 파일 읽기
int read(int fd, void *buffer, unsigned size) {
	check_address(buffer);
	int result = 0;

	if (fd == 0) {
		result = input_getc();
	}
	else if (fd == 1) {
		return -1;
	}
	else {
		struct file *f = process_get_file(fd);
		#ifdef VM
    		struct page *read_page = spt_find_page(&thread_current()->spt, buffer);
      		if(read_page && !read_page->writable){
        		exit(-1);
    	}
    	#endif
			if (f == NULL) {
				return -1;
			}
		lock_acquire(&filesys_lock);
		result = file_read(f, buffer, size);
		lock_release(&filesys_lock);
	}
	return result;
}

// 파일 쓰기
int write(int fd, const void *buffer, unsigned size)
{
	check_address(buffer);
	int result = 0;

	if (fd == 1) {
		putbuf(buffer, size);
		result = size;
	}
	else if (fd == 0) {
		return -1;
	}
	else {
		struct file *f = process_get_file(fd);
		if (f == NULL) {
			return -1;
		}
		lock_acquire(&filesys_lock);
		result = file_write(f, buffer, size);
		lock_release(&filesys_lock);
	}
	return result;
}

// 파일 위치 변경
void seek(int fd, unsigned position){
	if (fd < 2) { // 예약된 파일은 변경 불가
		return;
	}
	struct file *f = process_get_file(fd);
	if (f == NULL) {
		return;
	}
	file_seek(f, position);
}

// 파일 현재 위치 반환
unsigned tell(int fd) {
	if (fd < 2) { // 예약된 파일은 변경 불가
		return;
	}
	struct file *f = process_get_file(fd);
	if (f == NULL) {
		return;
	}
	return file_tell(f);
}

// 파일 닫기
void close(int fd) {
	if (fd < 2) { // 예약된 파일은 변경 불가
		return;
	}
	struct file *f = process_get_file(fd);
	if (f == NULL) {
		return;
	}
	file_close(f);
	process_close_file(fd); // fdt에서 제거하기
}

void *
mmap(void *addr, size_t length, int writable, int fd, off_t offset) {
	// printf("[mmap] start \t\t\t| [syscall.c:327]\n");
	if (!addr || addr != pg_round_down(addr))
		return NULL;
	if (offset != pg_round_down(offset))
		return NULL;
	if (!is_user_vaddr(addr) || !is_user_vaddr(addr + length))
		return NULL;
	if (spt_find_page(&thread_current()->spt, addr))
		return NULL;
	
	struct file *f = process_get_file(fd);
	if (f == NULL)
		return NULL;
	if (file_length(f) == 0 || (int)length <= 0)
		return NULL;
	// printf("[mmap] end \t\t\t| [syscall.c:327]\n");
	return do_mmap(addr, length, writable, f, offset);
}

void
munmap(void *addr) {
	// printf("[m-unmap] start \t\t\t| [syscall.c:347]\n");
	do_munmap(addr);
	// printf("[m-unmap] end \t\t\t| [syscall.c:347]\n");
}
