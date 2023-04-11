pos = [0] * 8
flag = [False] * 8
# print(flag)


def put():
    for i in range(8): #0-7
        print(f'{pos[i]:2}', end='')
    print()
    

def set(i):
    for j in range(8):
        if not flag[j]:
            pos[i] = j # Q를 j행에 배치
            if i == 7:
                put()
            else:
                flag[j] = True
                set(i + 1)
                flag[j] = False
        
set(0)
  