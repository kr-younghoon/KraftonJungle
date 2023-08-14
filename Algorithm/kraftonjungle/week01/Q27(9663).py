#### N-Queen #####

# import sys
# input = sys.stdin.readline

# n = int(input())
# row = [0] * n

# def check(x, row):
#     for i in range(x): 
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
#             return False
#     return True

# def dfs(x, n, row):
#     result = 0

#     if n == 1:
#         return 1
#     elif n == 2 or n == 3:
#         return 0
    
#     if x == n:
#         return 1
#     else:
#         for i in range(n):
#             row[x] = i
#             if check(x, row):
#                 result = result + dfs(x + 1, n, row)
#     return result
# print(dfs(0, n, row))

import sys
n = int(sys.stdin.readline())
# row 리스트에서 인덱스 = 행번호 / row[i] 값은 열번호
row = [0] * n
result = 0
# https://seongonion.tistory.com/103 참고
# https://lighter.tistory.com/m/26 참고
# 퀸을 놓을 수 있는 위치인지 여부 판단
def isPromising(x) :
    for i in range(x) :
        '''
        1. 같은 열에 있는지 확인
            row[x] == row[i] : x번 행과 i번 행에 놓여있는 퀸의 열 번호가 같은 경우
        2. 대각선에 존재하는지 확인
            row[x]-row[i] : 세로로 얼마만큼 갔는지
            x-i : 가로로 얼마만큼 갔는지
            위의 두 값이 같은 경우 대각선 상에 존재한다.
        '''
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i) :
            return False
    return True
# x = 행, row[x] = 열
def nQueens(x) :
    global result
    # x가 n이 되면 모든 행에 퀸이 채워졌다는 의미로 함수 종료
    if x == n :
        result += 1
        return
    else :
        for i in range(n) :
            row[x] = i
            if isPromising(x) :
                nQueens(x+1)
nQueens(0)
print(result)