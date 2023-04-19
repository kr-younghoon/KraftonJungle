import sys
import heapq
input = sys.stdin.readline

A = B = []
N = int(sys.stdin.readline())

for _ in range(N):
    input_num = int(sys.stdin.readline())
    if len(A) == len(B):
        heapq.heappush(A,-input_num)
    else:
        heapq.heappush(B,input_num)

    if B:
        while(-A[0] > B[0]):
            min_B = heapq.heappop(B)
            max_A = -(heapq.heappop(A))

            heapq.heappush(A,-min_B)
            heapq.heappush(B,max_A)

    print(-A[0])