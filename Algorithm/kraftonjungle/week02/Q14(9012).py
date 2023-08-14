import sys
input = sys.stdin.readline

# 괄호 문자열 Vaild PS, VPS
time = int(input())
for i in range(time):
    vps = input()
    stack = []
    check = False
    for i in range(len(vps)-1):
        if vps[i] == '(':
            stack.append('(')
        else:
            if stack:
                if stack.pop() == '(' and vps[i] == ')':
                    check = True
                else:
                    check = False
                    break
            else:
                check = False
                break
            
    if stack:
        check
    print('YES') if check else print('NO')