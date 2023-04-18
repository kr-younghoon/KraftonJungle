from collections import deque

queue = deque(x+1 for x in range(int(input())))

print(queue)