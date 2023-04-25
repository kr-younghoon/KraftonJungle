import sys
input = sys.stdin.readline
    

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
            
n = int(input())
m = int(input())

cnt = 0
visited = [0]*(n+1)
graph = [[] * n for _ in range(n+1)]
            
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
dfs(1)
print(cnt)

