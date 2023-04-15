N = int(input())
A = list(map(int,input().split()))

Len = [0] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i] and Len[i] < Len[j]:
            Len[i] = Len[j]
    Len[i] += 1

print(max(Len))