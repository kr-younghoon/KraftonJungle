#x는 필수가 아니게 하고 싶은데 기억이 안난다.
def factorial(num: int, x: int):
    if num > 0:
        factorial(num-1, x * num)
    
    if num == 0:
        print(x)

n = int(input())
        
factorial(n, 1)