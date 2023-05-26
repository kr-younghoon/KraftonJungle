# 내리막길 https://www.acmicpc.net/problem/1520 
'''
예제 입력 1 : 
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

예제 출력 1 : 3
'''
import sys
input = sys.stdin.readline
# 첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.
sys.setrecursionlimit(10 ** 9)

def dfs(sx, sy):
    # 도착
    if sx == M - 1 and sy == N - 1:
        return 1
    
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    ways = 0
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[sx][sy] > graph[nx][ny]:
            ways += dfs(nx, ny)
            
    dp[sx][sy] = ways
    return dp[sx][sy]
        

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

print(dfs(0,0))