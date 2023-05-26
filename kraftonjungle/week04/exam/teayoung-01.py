#점프 1890번

import sys
input = sys.stdin.readline


n = int(input())
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1 #처음 경우의 수는 1로 저장


for i in range(n):
    #열
    for j in range(n):
    #행    
        if i == n-1 and j == n-1:#for문 범위 설정
            break
        jump = game_map[i][j]#game맵 좌표값만큼 행열 값을 jump변수에 넣어주고    
        if j+jump < n:
            dp[i][j+jump] += dp[i][j]#dp에서 jump값을 더 한 행 dp에 경우의 수를 추가해준다.
        if i+jump < n:
            dp[i+jump][j] += dp[i][j]#dp에서 jump값을 더 한 열 dp에 경우의 수를 추가해준다.


print(dp[n-1][n-1])