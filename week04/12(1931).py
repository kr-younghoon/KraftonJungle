 # Q1931 - 회의실 배정
# sort와 sorted 의 차이 ?

# (정답코드) CASE 1 . sorted 를 쓴 case : sorted 를 쓴 후에 key = lambda로 우선순위를 고정하였다.
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]] list()
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)] tuple()

'''
N = int(input())
check_list = sorted([tuple(map(int, input().split())) for _ in range(N)], key= lambda x: (x[1], x[0]))
print(check_list)
cnt = end = 0
for s, e in check_list:
    if s >= end:
        cnt += 1
        end = e
print(cnt)
'''

# (오답코드) CASE 2 . sort를 쓴 case : sort를 썼다.
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

'''
N = int(input())
check_list = [list(map(int, input().split())) for _ in range(N)]
check_list.sort(key= lambda x: (x[1], x[0]))
print(check_list)
cnt = end = 0
for s, e in check_list:
    if s >= end:
        cnt += 1
        end = e
print(cnt)
'''

# ? (해결)
# -> lambda로 정렬 기준을 뒤에꺼부터 이후 겹치면 앞에꺼 기준으로 정렬 기준을 정해줘야한다.

