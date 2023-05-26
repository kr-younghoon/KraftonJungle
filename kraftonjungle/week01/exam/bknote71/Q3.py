# 부분수열의합

# 5 0
# -7 -3 -2 5 8

N, S = map(int, input().split())
seq = list(map(int, input().split()))

result = []
count = 0


def sumList(arr):
    if sum(arr) == S:
        return True
    return False


def solution(n, leftCount, prev):
    global count
    if leftCount == 0 and sumList(result):
        count += 1
        return

    for i in range(prev + 1, n):
        result.append(seq[i])
        solution(n, leftCount-1, i)
        result.pop()


for i in range(1, N+1):
    solution(N, i, -1)

print(count)