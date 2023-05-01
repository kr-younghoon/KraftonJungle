import sys

n = int(sys.stdin.readline())

num_list = [0] * 10001  # index가 0부터 시작이므로 10001개 생성

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1  # 배열마다 각 숫자가 들어감
    
for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)