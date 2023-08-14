import sys
input = sys.stdin.readline


N = int(input().strip())
Q = []

for i in range(N):
    order = input().split()
    running = order[0]
    
    if "push" == running:
        Q.append(order[1])
    elif "pop" == running:
        if Q:
            print(Q.pop())
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
    elif "top" == running:
        if Q:
            print(Q[-1])
        else:
            print(-1)
    else:
        pass