def fsort(a, max):
    
    n = len(a) # 정렬할 배열 a
    f = [0] * (max + 1)
    b = [0] * n
    
    for i in range(n): f[a[i]] += 1
    for i in range(1, max + 1): f[i] += f[i - 1]
    for i in range(n - 1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]
    for i in range(n): a[i] = b[i]
    
def counting_sort(a):
    fsort(a, max(a))
    
if __name__ == "__main__":
    num = int(input())
    x = [None] * num
    
    for i in range(num):
        while True:
            x[i] = int(input())
            if x[i] >= 0: break
    
    counting_sort(x)

    for i in range(num):
        print(f'{x[i]}')
    