# # ex | 55 - 50 + 40

# in_line = input().split('-')  # ["55", "50 + 40"]
# num = [] # 리스트 선언
# for i in in_line: # for "55", "50 + 40" - 2 times
#     cnt = 0 # count 
#     s = i.split("+") # 55, 50, 40?
#     for j in s: # 55, 50, 40
#         cnt += int(j) 
#     num.append(cnt)
# n = num[0]
# for i in range(1, len(num)):
#     n -= num[i]
# print(n)


in_line = ["55", "50 + 40"]
for i in in_line:
    cnt = 0
    print(f"19line - call (i) :: {i}")
    s = i.split("+")
    print(f"21line - call (s) :: {s}")
    
    for j in s:
        print(f"23line - call (j) :: {j}")
        
        cnt += int(j)
    print(cnt)