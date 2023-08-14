N, M = map(int, input().split()) # 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다.
tree_list = list(map(int, input().split()))
sum = 0

lt, rt = 0, max(tree_list)

while lt <= rt:
    mid = (lt + rt) // 2
    sum = 0    
    
    for i in tree_list:
        if sum >= M:
            break
        if i > mid:
            sum = sum + (i - mid)
    
    if sum >= M:
        lt = mid + 1
    elif sum < M:
        rt = mid - 1
print(rt)