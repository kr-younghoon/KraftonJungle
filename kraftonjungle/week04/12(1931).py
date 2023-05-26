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

'''
GPT

만약 끝나는 시간만으로 정렬했다면, 끝나는 시간이 같은 회의들 중에서 어떤 회의를 먼저 배정해야 할지 알 수 없기 때문에 
최대 회의 수를 보장할 수 없습니다. 따라서 끝나는 시간을 기준으로 먼저 정렬하고, 이후에 겹치는 회의들이 있는 경우에는 
시작하는 시간을 기준으로 다시 정렬해줘야 합니다. 이때 lambda를 사용하여 정렬 기준을 뒤에꺼부터 정렬하고, 
이후에 겹치는 경우에는 앞에꺼 기준으로 다시 정렬해주는 것입니다. 이렇게 하면 최대한 많은 회의를 배정할 수 있습니다.
'''