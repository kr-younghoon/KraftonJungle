times = int(input())
save_qlist = []
score = 1
whole_score = 0


for i in range(1, times+1):
    x = input()
    for i in x:
        if i == "O":
            whole_score += score
            score += 1
        else:
            score = 1
    save_qlist.append(int(whole_score))
    whole_score = 0
    score = 1
    

for i in save_qlist:
    print(i)