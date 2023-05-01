import sys
input = sys.stdin.readline


N = int(input())

def recursive(total, mid, N):
    
    if N <= 3:
        return "moo"[N-1]
   
    left = (total - mid) // 2
    
    if N <= left:
        return recursive(left, mid - 1, N)
    if N > left + mid:
        return recursive(left, mid - 1, N - left - mid)
    if N - left == 1:
        return "m"
    else:
        return "o"
    

total = 3
n = 0
while total < N:
    n += 1
    total = 2 * total + n + 3


print(recursive(total, n+3, N))
