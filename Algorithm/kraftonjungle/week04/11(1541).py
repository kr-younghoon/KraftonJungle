# ex | 55 - 50 + 40

in_line = input().split('-')  # ["55", "50 + 40"]
num = [] # 리스트 선언
for i in in_line: # for "55", "50 + 40" - 2 times
    cnt = 0 # count 
    s = i.split("+") # 1set 55 // 2set 50, 40
    for j in s: # 55 // 50, 40
        cnt += int(j) # 90 
    num.append(cnt) # cnt = 55 / 90 append
n = num[0] # n = num[0] -> 55
for i in range(1, len(num)): # range -> 1
    n -= num[i] # 55 - 90 = -35
print(n) # 이예야