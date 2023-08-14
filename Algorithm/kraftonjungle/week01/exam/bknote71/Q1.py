# 더하기 사이클

N = int(input())
start = N
count = 0


def solution(n):
    global count
    newN = (n % 10)*10 + (n//10 + n % 10) % 10
    count += 1
    if (newN == N):
        return
    return solution(newN)


solution(N)

print(count)