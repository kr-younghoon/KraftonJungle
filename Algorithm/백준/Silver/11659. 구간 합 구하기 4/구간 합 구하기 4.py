# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 5 3
num_list = list(map(int,input().split()))
S = [0] # 합을 저장하는 리스트

#구간 합 S[5] = num_list[1-5]까지 합을 저장한다.
for num in range(N):
    S.append(S[-1] + num_list[num])

for _ in range(M):
    i, j = map(int, input().split())
    print(S[j] - S[i - 1])
    