# 피보나치 수 2 - Q2748
'''
예제 입력1 : 10
예제 출력1 : 55
'''

import sys
input = sys.stdin.readline


n = int(input())
fibonacci_list = []
num = 0

while (True):
    if (num == 0):
        fibonacci_list.append(0)
        fibonacci_list.append(1)
    elif (num > 1):
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
    if (num == n):
        print(fibonacci_list[-1])
        break
    num += 1