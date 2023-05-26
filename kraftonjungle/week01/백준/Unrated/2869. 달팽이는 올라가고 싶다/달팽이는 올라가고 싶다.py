import math

# A / B / V 
A, B, V = map(int, input().split())

start = 0
day = 0

# while True:
#     day += 1
#     start += A
#     if (start >= V):
#         break
#     start -= B

day = math.ceil((V - B) / (A - B))

    
print(f"{day}")