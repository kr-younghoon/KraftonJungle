import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
Q = deque([])

for i in range(N):
    order = input().split()
    running = order[0]
    
    if "push" == running:
        Q.append(order[1])
    elif "pop" == running:
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif "size" == running:
        print(len(Q))
    #?????
    elif "empty" == running:
        if Q:
            print(0)
        else:
            print(1)
    elif "front" == running:
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif "back" == running:
        if not Q:
            print(-1)
        else:
            print(Q[-1])
    else:
        
        pass