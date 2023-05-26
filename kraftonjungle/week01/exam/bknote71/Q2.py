# 1, 2, 3 더하기

N = int(input())
testCases = [int(input()) for _ in range(N)]


def solution(N):
    if N == 0:
        return 1

    leftNumber = 0
    for i in range(1, 4):
        if N - i >= 0:
            leftNumber += solution(N-i)
    return leftNumber


for case in testCases:
    print(solution(case))