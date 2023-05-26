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
graph = [list(map(int, input().split())) for _ in range(N)] # input graph
dp = [[0] * N for _ in range(N)] # 횟수 카운트
dp[0][0] = 1


for i in range(N): # 0 - 3 / 4times
    for j in range(N): # 0 - 3 / 4times
        if i == (N - 1) and j == (N - 1): # if stop : i or j => 3
            print(dp[i][j]) # dp[0][0] -> 1 , dp[3][3] = 3
            break
        # right
        if j + graph[i][j] < N: # j 좌표에서 기존 지점의 숫자만큼 움직일때, N보다 작아야함
            dp[i][j + graph[i][j]] += dp[i][j] 
            
        # down
        if i + graph[i][j] < N: # i 좌표에서 기존 지점의 숫자만큼 움직일때, N보다 작아야함
            dp[i + graph[i][j]][j] += dp[i][j]
            