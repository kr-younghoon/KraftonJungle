# 2667번 : 단지번호붙이기
'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])