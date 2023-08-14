import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def hello(N, k, d):
    if k == 0:
        return 1
    elif k == 1:
        return N % d
    
    tmp = hello(N, k//2, d)
    if k % 2:
        return (tmp * tmp * N) % d
    else:
        return (tmp * tmp) % d
    
print(hello(A, B, C))