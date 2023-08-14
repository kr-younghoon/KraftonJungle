def move(n, a, b, c):
    if n == 1:
        print(f"{a} {c}")
        return
    
    move(n-1, a, c, b)
    print(f"{a} {c}")
    move(n-1, b, a, c)

n = int(input())
t = pow(2, n) - 1
print(t)

if n <= 20:
    move(n, 1, 2, 3)