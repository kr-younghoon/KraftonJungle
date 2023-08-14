import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
binary_tree = []
while True:
    try:
        binary_tree.append(int(input()))
    except:
        break
def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if binary_tree[start] < binary_tree[i]:
            mid = i
            break
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(binary_tree[start])
postorder(0, len(binary_tree) - 1)