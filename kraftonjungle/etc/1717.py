# 집합의 표현 - 1717
# 초기에 n + 1 개의 집합 {0}, {1}, {2}, ... , {n}
import sys 
input = sys.stdin.readline

# 첫줄 n, m / lst 선언
n, m = map(int, input().split())
lst = []

# n개의 리스트 추가
for i in range(n):
    list.append(i)
  
print(lst)  

# 반복문 m 개의 줄 각각의 연산.
# for i in range(m):
#     v, a, b = map(int, input().split())
#     if (v == 0):
#         print("0")
#         # a와 b의 집합이 합쳐진다.
        
#     elif (v == 1):
#         print("1")
#         # a와 b가 한 집합 안에 같이 있는지 확인한다.

    