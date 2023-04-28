# 1388번 바닥 장식
'''
예제 입력 1 : 

4 4
----
----
----
----
'''

import sys
input = sys.stdin.readline

def dfs(x, y):
    if graph[x][y] == '|':
        graph[x][y] = 1
        for i in [1, -1]:
            side_check_x = x + i
            if (side_check_x > 0 and side_check_x < N) and graph[side_check_x][y] == '|':
                dfs(side_check_x, y)
    if graph[x][y] == '-':
        graph[x][y] = 1
        for j in [1, -1]:
            side_check_y = y + j
            if (side_check_y > 0 and side_check_y < M) and graph[x][side_check_y] == '-':
                dfs(x,side_check_y)
            

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

answer = 0

for k in range(N):
    for l in range(M):
        if graph[k][l] == '-' or graph[k][l] == '|':
            dfs(k, l)
            answer += 1



print(answer)