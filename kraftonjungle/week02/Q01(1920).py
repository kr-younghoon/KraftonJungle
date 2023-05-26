# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1920%EB%B2%88-%EC%88%98-%EC%B0%BE%EA%B8%B0-Python

# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력 
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력 - M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 예제 입력 1
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# 예제 출력 1
# 1 1 0 0 1

# 1920 하 이분탐색(3-3 , 9) - 수 찾기 

# def bin_search(element, some_list, start = 0, end = None):
#     if end == None:
#         end = len((some_list) - 1)
#     if start > end:
#         return 0
    
#     mid = (start + end) // 2
    
#     if element == some_list[mid]:
#         return 1
#     elif element < some_list[mid]:
#         end = mid - 1
#     elif element > some_list[mid]:
#         start = mid + 1
#     return bin_search(element, some_list, start, end)

# n = int(input())
# n_list = list(map(int, input().split()))
# sorted_list = sorted(n_list)

# m = int(input())
# m_list = list(map(int, input().split()))

# for i in range(len(m_list)):
#     print(bin_search(m_list[i], sorted_list))

# 입력
N = int(input()) # 자연수 N개 주어지는지 
A = list(map(int, input().split()))
M = int(input()) # 자연수 M개 주어지는지
arr = list(map(int, input().split()))
A.sort()			# A 정렬

for num in arr:
    lt, rt = 0, N - 1
    isExist = False
    
    while lt <= rt:
        mid = (lt + rt) // 2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    
    if not isExist:
        print(0)


