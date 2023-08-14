# 5639번 이진 검색 트리 (https://www.acmicpc.net/problem/5639)
import sys
input = sys.stdin.readline

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

def postorder(s, e):
    if s > e:
        return
    mid = e + 1 # 오른쪽 노드가 없을 경우
    
    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break
    
    postorder(s+1, mid-1)
    postorder(mid, e)
    print(nums[s])
postorder(0, len(nums)-1)
    