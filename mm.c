/* mm-naive.c - The fastest, least memory-efficient malloc package.
 * 
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 */

// NEXT-FIT 구현

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "TEAM 3",
    /* First member's full name */
    "LEE YOUNGHOON",
    /* First member's email address */
    "sullanta0802@gmail.com",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""
};


// Basic constants and macros 
// [기본 상수와 매크로]
#define WSIZE 4 
// 1워드 | 워드, 헤더 푸터의 크기를 선언합니다. 블록의 크기와 관련된 정보를 저장합니다.
#define DSIZE 8 
// 2워드 | 더블워드, 주소 정보를 저장합니다.
#define CHUNKSIZE (1<<12) 
// 초기 가용 블록과 힙 확장을 위한 기본 크기 | 2^12(4096bytes), 힙을 확장할 때 사용되는 양

#define MAX(x, y) ((x) > (y)? (x) : (y)) // 큰 값을 반환
/* x가 y보다 큰지 비교하고 Boolean값을 ?(삼항 연산자)로 
 * 결과가 참인 경우 x를 반환, 거짓인 경우 y를 반환합니다. 
 */

// Pack a size and allocated bit into a word 
// [크기와 할당 비트를 하나의 워드에 압축하는 것]
#define PACK(size, alloc) ((size) | (alloc)) 
// -> 워드(Header or Footer)에  할당정보(0,1)와 크기(메모리 블록의 크기) 저장할 값 반환
// 비트 OR연산자로 "|"를 사용하여 size와 alloc의 비트를 결합하여 하나의 워드에 패킹된 값을 생성합니다.
// 그렇게 하여 크기와 할당 정보를 하나의 워드에 저장

// Read and wirte a word at address p 
// [주소 p에서 워드를 읽고 쓰는 것]
#define GET(p) (*(unsigned int *)(p)) // p가 참조하는 word를 반환한다. 
#define PUT(p, val) (*(unsigned int *)(p) = (val)) // p가 가리키는 word에 val 저장.
// unsigned int -> 부호가 없는 정수를 나타내는 데이터 형식.  (0 - 4bytes..32bit(4,294,967,295))

// READ THE SIZE AND ALLOCATED FIELDS FROM ADDRESS p 
// [주소 p에서 크기와 할당 필드를 읽는 것]
#define GET_SIZE(p) ((GET(p)) & ~0x7) // p가 가리키는 block size 반환
// 마지막 3비트를 0으로 만들어 크기 필드를 추출합니당
#define GET_ALLOC(p) ((GET(p)) & 0x1) // p가 가리키는 block의 할당 비트 반환
// 읽어온 워드에서 마지막 비트(이진수로 1)을 추출하는 역할!

// Given block ptr bp, compute address of its header and footer 
// [주어진 블록 포인터 bp를 기반으로 해당 블록의 헤더와 푸터 주소를 계산하는 것]
#define HDRP(bp) ((char *)(bp) - WSIZE) 
// bp가 가리키는 block의 Header를 가리키는 포인터 변환
#define FTRP(bp) ((char *)(bp) + GET_SIZE(HDRP(bp)) - DSIZE)
// bp가 가리키는 block의 Footer를 가리키는 포인터 반환

// GIVEN block ptr bp, compute address of next and previous blocks
// [주어진 블록 포인터 bp를 기반으로 다음 블록과 이전 블록의 주소를 계산하는 것]
#define NEXT_BLKP(bp) ((char *)(bp) + GET_SIZE((char *)(bp) - WSIZE))
// 다음 block pointer(주소) 반환
#define PREV_BLKP(bp) ((char *)(bp) - GET_SIZE(((char *)(bp) - DSIZE)))
// 이전 block pointer(주소) 반환


static void *extend_heap(size_t words);
static void *coalesce(void *bp);
static void *find_fit(size_t asize);
static void place(void *bp, size_t asize);

static void *heap_listp;
static char *nextfit;


/* 
 * mm_init - initialize the malloc package.
 */
int mm_init(void)
{
    if ((heap_listp = mem_sbrk(4 * WSIZE)) == (void *)-1)
        return -1;
    PUT(heap_listp, 0); // Alignment padding
    PUT(heap_listp + (1 * WSIZE), PACK(DSIZE, 1));
    PUT(heap_listp + (2 * WSIZE), PACK(DSIZE, 1));
    PUT(heap_listp + (3 * WSIZE), PACK(0, 1));
    heap_listp += (2 * WSIZE);

    // Extend the empty heap with a free block of CHUNKSIZE bytessš
    if (extend_heap(CHUNKSIZE/WSIZE) == NULL) {
        return -1;
    }
    nextfit = heap_listp;
    return 0;
}

static void *extend_heap(size_t words) {
    char *bp;
    size_t size;

    // Allocate an even number of words to maintain alignment
    size = (words % 2) ? (words + 1) * WSIZE : words * WSIZE;
    if ((long)(bp = mem_sbrk(size)) == -1)
        return NULL;
    
    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1));

    return coalesce(bp);
}

/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t asize;
    size_t extendsize;
    char *bp;

    if (size == 0)
        return NULL;

    if (size <= DSIZE)
        asize = 2 * DSIZE;
    else
        asize = DSIZE * ((size + (DSIZE) + (DSIZE - 1)) / DSIZE);

    if ((bp = find_fit(asize)) != NULL) {
        place(bp, asize);
        return bp;
    }

    extendsize = MAX(asize, CHUNKSIZE);
    if ((bp = extend_heap(extendsize/WSIZE)) == NULL)
        return NULL;
    place(bp, asize);
    return bp;
}



static void *find_fit(size_t asize) {
    char *bp = nextfit;

    while(GET_SIZE(HDRP(bp)) > 0) {
        if (!GET_ALLOC(HDRP(bp)) && (GET_SIZE(HDRP(bp)) >= asize)) {
            nextfit = bp;
            return bp;
        }
        bp = NEXT_BLKP(bp);
    }

    bp = heap_listp;
    while (bp < nextfit) {
        if(!GET_ALLOC(HDRP(bp)) && (GET_SIZE(HDRP(bp)) >= asize)) {
            nextfit = bp;
            return bp;
        }
        bp = NEXT_BLKP(bp);
    }
    return NULL;
}



static void place(void *bp, size_t asize) {
    size_t csize = GET_SIZE(HDRP(bp));

    if ((csize - asize) >= (2 * DSIZE)) {
        PUT(HDRP(bp), PACK(asize, 1));
        PUT(FTRP(bp), PACK(asize, 1));

        bp = NEXT_BLKP(bp);
        PUT(HDRP(bp), PACK(csize - asize, 0));
        PUT(FTRP(bp), PACK(csize - asize, 0));
        nextfit = bp;
    }
    else {
        PUT(HDRP(bp), PACK(csize, 1));
        PUT(FTRP(bp), PACK(csize, 1));
    }
}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *bp)
{
    size_t size = GET_SIZE(HDRP(bp));

    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    coalesce(bp);
}

static void *coalesce(void *bp) {
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp)));
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size_t size = GET_SIZE(HDRP(bp));

    if (prev_alloc && next_alloc) {
        return bp;
    }

    else if (prev_alloc && !next_alloc) {
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
    }

    else if (!prev_alloc && next_alloc) {
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        PUT(FTRP(bp), PACK(size, 0));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
    }

    else {
        size += GET_SIZE(HDRP(PREV_BLKP(bp))) +
            GET_SIZE(FTRP(NEXT_BLKP(bp)));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        PUT(FTRP(NEXT_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
    }
    nextfit = bp;
    return bp;
}

/*
 * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
 */
void *mm_realloc(void *ptr, size_t size) {
    void *oldptr = ptr;
    void *newptr;
    size_t copySize;
    
    newptr = mm_malloc(size);
    // if (newptr == NULL)
    //   return NULL;
    // copySize = *(size_t *)((char *)oldptr - SIZE_T_SIZE);
    // if (size < copySize)
    //   copySize = size;
    // memcpy(newptr, oldptr, copySize);
    // mm_free(oldptr);
    // return newptr;
    if (newptr == NULL) // 새로운 메모리 블록 할당에 실패한 경우
      return NULL; // 함수 종료
    copySize = GET_SIZE(HDRP(ptr)); // 이전 메모리 블록의 크기 가져오기
    if (size < copySize) // 요청 된 크기가 복사할 크기보다 작은 경우
      copySize = size; // 복사사이즈를 사이즈로 조정
    memcpy(newptr, oldptr, copySize); // 이전 메모리 블록의 데이터를 새로운 메모리 블록으로 복사
    mm_free(oldptr); // 이전 메모리 블록을 해제
    return newptr; // 새로운 메모리 블록의 포인터 반환
}