# 제한
# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2N

# 예제 입력 1 복사
# 2 3 1
# 예제 출력 1 복사
# 11
# 예제 입력 2 복사
# 3 7 7
# 예제 출력 2 복사
# 63
# 예제 입력 3 복사
# 1 0 0
# 예제 출력 3 복사
# 0
# 예제 입력 4 복사
# 4 7 7
# 예제 출력 4 복사
# 63
# 예제 입력 5 복사
# 10 511 511
# 예제 출력 5 복사
# 262143
# 예제 입력 6 복사
# 10 512 512
# 예제 출력 6 복사
# 786432

# Z 문제(1074)
# 한수는 크기가 2**N × 2**N인 2차원 배열을 Z모양으로 탐색하려고 한다. 
# 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# N > 1인 경우, 배열을 크기가 2**(N-1) × 2**(N-1)로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# 다음 예는 2**2 × 2**2 크기의 배열을 방문한 순서이다. (사진1)
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
# 다음은 N=3일 때의 예이다. (사진2)

# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.
# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def asdf(N, r, c):
    if N == 0:
        return 0
    yaho = 2 ** (N-1)
     
    if r < yaho and c < yaho:
        return asdf(N-1, r, c)
    elif r < yaho and yaho <= c:
        return yaho * yaho + asdf(N-1, r, c-yaho)
    elif yaho <= r and c < yaho:
        return 2 * yaho * yaho + asdf(N-1, r-yaho, c)
    elif yaho <= r and yaho <= c:
        return 3 * yaho * yaho + asdf(N-1, r-yaho, c-yaho)

print(asdf(N, r, c))

N, r, c = map(int, input().split())

def search(N, r, c):
    if N==0: return 0
    M=2**(N-1)
    if r<M and c<M: 
        return search(N-1, r, c)
    elif r<M and M<=c: 
        return M*M+search(N-1, r, c-M)
    elif M<=r and c<M: 
        return 2*M*M+search(N-1, r-M, c)
    elif M<=r and M<=c: 
        return 3*M*M+search(N-1, r-M, c-M)

print(search(N, r, c))