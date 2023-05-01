import sys
input = sys.stdin.readline

S = input()
stc = []

for i in S:
    stc.append(i)
    
    if stc[-4:] == ["P", "P", "A", "P"]:
        stc.pop() # delete P
        stc.pop() # delete A
        stc.pop() # delete P

if stc == ["P", "\n"]:
    print("PPAP")
else:
    print("NP")