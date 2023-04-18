import sys
input = sys.stdin.readline
from collections import deque


# N = int(input())
# Q = [i for i in range(1, N+1)]
# count = 0
# print(Q)

# while len(Q) != 1:
#     j = Q[count]
    
#     if (j % 2 == 0): #짝수일때
#         Q.append(Q.pop(0))
#     elif (j % 2 != 0): #홀수일때
#         Q.pop(0)
    
#     count += 1
    
    



# print(Q[0])
from collections import deque

queue = deque(x+1 for x in range(int(input())))

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])