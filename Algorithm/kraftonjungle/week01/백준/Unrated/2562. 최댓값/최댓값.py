count_num = 0
max = 0
num_list = []

#9개의 자연수
for i in range(1,10):
    j = int(input())
    num_list.append(j)
    if j > max:
        max = j
        count_num = i
        
print(f"{max}\n{count_num}")