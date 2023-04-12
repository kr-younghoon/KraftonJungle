# 수 정렬 하기 3

# 도수 정렬로 풀어햐나, 정석적으로 풀면 메모리 초과가 뜨는 Q
# 공간복잡도를 줄이는 형식으로 풀어야하는 문제

# 예제 입력 1
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7

#예제 출력
# 1\n1\n2\n2\n3\n3\n4\n5\n5\n7

# 도수 정렬은 시간복잡도가 O(n)으로 비록, 최댓값이 존재해야 쓸수있지만,
# 퀵정렬 , 병합정렬 , 힙 정렬 O(n*logn)보다 빠르게 정렬할 수 있다.

import sys
input = sys.stdin.readline

n = int(input()) #count
f = [0] * 10001 #max

for i in range(n):
    f[int(input())] += 1
    # input_num = int(input())
    # f[input_num - 1] = f[input_num - 1] + 1
    # 같은 느낌.
    
for j in range(10001): #10001 
    if f[j] != 0: # f[0] - f[10000]이 0이 아닐때 // 속이 빈것을 제외처리
        for k in range(f[j]): # 바로 프린트 / 정렬 없이 처리하는듯?
            print(j) 

import sys
input = sys.stdin.readline

n = int(input())
f = [0] * 10001 

for i in range(n):
    f[int(input())] += 1
for j in range(10001):
    if f[j] != 0:
        for k in range(f[j]):
            print(j)


# 클래식 교재 것들을 처리함
# 백준에서는 메모리 초과 이슈

# import sys
# input = sys.stdin.readline

# def fsort(a, max):
    
#     n = len(a) # 정렬할 배열 a
#     f = [0] * (max + 1)
#     b = [0] * n
    
#     for i in range(n): f[a[i]] += 1
#     for i in range(1, max + 1): f[i] += f[i - 1]
#     for i in range(n - 1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]
#     for i in range(n): a[i] = b[i]
    
# def counting_sort(a):
#     fsort(a, max(a))
    
# if __name__ == "__main__":
#     num = int(input())
#     x = [None] * num
    
#     for i in range(num):
#         while True:
#             x[i] = int(input())
#             if x[i] >= 0: break
    
#     counting_sort(x)

#     for i in range(num):
#         print(f'{x[i]}')
    