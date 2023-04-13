# def hanoi(no, a, b):
#     if ()
#     if (no > 1):
#         hanoi(no - 1 , a , 6 - a - b)
#     print(f"{no} {a} {b}")
    
#     if (no > 1):
#         hanoi(no - 1, 6 - a - b, b)
        
    
# n = 3

# hanoi(n, 1, 3)

# def hanoi(n, frm, tmp, to):
#     if n == 1:
#         print(str(frm) + " " + str(to))
#         return

#     hanoi(n - 1, frm, to, tmp)
#     print(str(frm) + " " + str(to))
#     hanoi(n - 1, tmp, frm, to)


# num = int(input())
# k = pow(2, num) - 1
# print(k)
# if num <= 20:
#     hanoi(num, 1, 2, 3)

#방법 1
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