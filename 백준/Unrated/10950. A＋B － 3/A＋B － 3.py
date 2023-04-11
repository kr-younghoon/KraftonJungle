T = int(input())
plus_list = []

for i in range(T):
    A,B = map(int, input().split())
    plus_list.append(A+B)
    
for i in plus_list:
    print(i)