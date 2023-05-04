# 점프 https://www.acmicpc.net/problem/1890 
''' 
예제 입력 1:
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
'''

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (0, 1)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == y == N - 1:
            print(dp[x][y])
            exit(0)
        dist = graph[x][y]
        if x + dist < N:
            dp[x + dist][y] += dp[x][y]
        if y + dist < N:
            dp[x][y + dist] += dp[x][y]