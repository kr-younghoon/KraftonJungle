N = int(input())
check_list = [list(map(int, input().split())) for _ in range(N)]
check_list.sort(key= lambda x: (x[1], x[0]))
cnt = end = 0
for s, e in check_list:
    if s >= end:
        cnt += 1
        end = e
print(cnt)