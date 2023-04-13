#정수 N개로 이루어진 수열 A, 정수 X
N, X = map(int, input().split())


input_short_list = map(int, input().split())

short_list = []
#A에서 X보다 작은 수를 모두 출력하는 프로그램

#(1<= N, X <= 10000)
if (1<= N <= 10000 and 1 <= X <= 10000):
    for i in input_short_list:
        if (X > i):
            short_list.append(i)

for i in short_list:
    print(i, end=" ")