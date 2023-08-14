#2805번 나무 자르기

# 입력 : 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다.
#(1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
# 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 떄문에,
# 상근이는 집에 필요한 나무를 항상 가져갈 수 있다.
# 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

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