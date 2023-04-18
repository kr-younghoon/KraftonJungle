import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
original = deque(x+1 for x in range(N))
final = []


while True:
    for i in range(1, K):
        original.append(original.popleft())
    final.append(original.popleft())
    if len(original) < 1:
        break

print("<", end="")
for i in final:
    if i != final[-1]:
        print(i, end=", ")
    else:
        print(i, end="")
print(">")
    
