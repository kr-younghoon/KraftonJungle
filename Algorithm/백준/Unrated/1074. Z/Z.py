N, r, c = map(int, input().split())

def search(N, r, c):
    if N==0: return 0
    M=2**(N-1)
    if r<M and c<M: 
        return search(N-1, r, c)
    elif r<M and M<=c: 
        return M*M+search(N-1, r, c-M)
    elif M<=r and c<M: 
        return 2*M*M+search(N-1, r-M, c)
    elif M<=r and M<=c: 
        return 3*M*M+search(N-1, r-M, c-M)

print(search(N, r, c))