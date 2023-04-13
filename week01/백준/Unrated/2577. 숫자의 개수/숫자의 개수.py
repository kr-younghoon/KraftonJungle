# input 3개 들어가야함 다 따로따로 움직일것
A = int(input())
B = int(input())
C = int(input())

#곱해서 문자열
multiple = str(A * B * C)

for i in range(0,10):
    number = str(i)
    print(multiple.count(number))