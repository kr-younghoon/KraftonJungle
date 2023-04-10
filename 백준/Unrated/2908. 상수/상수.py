ex_input = list(map(int, input().split()))
e_list = []
max = 0

# for i in ex_input:
#     ex_input
    

for i in ex_input:
    i = str(i)
    e_list.append(int(i[::-1]))
    
for i in e_list:
    j = int(i)
    if j >= max:
       max = i

print(max) 
