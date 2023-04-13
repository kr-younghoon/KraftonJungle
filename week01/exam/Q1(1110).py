# # plus cycle

# 문제
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 
# 다음 예를 보자.
# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 
# 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
# 출력 : 첫째 줄에 N의 사이클 길이를 출력한다.
# 예제 : (26/4) (55/3) (1/60) (0/1) (71/12)

# import sys
# input = sys.stdin.readline

# num = input()

# def plus_cycle(num):
#     a = b = c = 0
#     count = 0
    
#     while (count < 10):
#         if count == 0:
#             a, b = str(num)[0], str(num)[1]
#             print(f"29: a : {a}, b: {b}")
#             c = int(a) + int(b)
#             print(f"31: {a} + {b} = {c}")
#         elif count > 0:
#             a, b = b, str(c)[-1]
#             print(f"34: a: {a} b: {b}")
#             if (str(a) + str(b)) == str(num):
#                 break
#             c = int(a) + int(b)
#             print(f"36: {a} + {b} = {c}")
        
#         if c < 10:
#                 c = str("0") + str(c)
#                 print(f"39: {c}")
        

#         count += 1
#         print(f"35: {count}")
        
#     print(count)

# plus_cycle(num)

# def plus_cycle(num):
#     a = b = c = 0
#     count = 0
    
#     while (count < 100):
        
#         if count == 0:
#             c = num
#             if int(c) < 10:
#                 c = str("0") + str(c)
#             a, b = str(c)[0], str(c)[1]
#         if count > 0:
#             a, b = b, str(c)[-1]
#             if num == a + b:
#                 break
#         c = int(a) + int(b)  
#         if (len(num) < 10 or c < 10):
#             c = str("0") + str(c)
             

#         count += 1
#     print(count)
    
# plus_cycle(num)

import sys
input = sys.stdin.readline

n = input()
num = n
count = 0

while True:
    if len(num) == 1:
        num = "0" + num
    plus = str(int(num[0]) + int(num[1]))
    num = num[-1] + plus[-1]
    count += 1
    if num == n:
        print(count)
        break
    