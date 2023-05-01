from collections import deque

queue = deque(x+1 for x in range(int(input())))

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])