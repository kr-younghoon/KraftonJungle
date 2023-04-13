count = int(input())
insert_num = list(map(int, input().split()))
n = 0

for i in insert_num:
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                n += 1
            break
        
print(n)


