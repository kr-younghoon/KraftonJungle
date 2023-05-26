import sys
input = sys.stdin.readline
# 예제를 보니, stack의 구조는 LIFO(가장 나중에 데이터가 
# 가장 먼저 꺼내지는 방식으로 0으로 삭제시에 나중의 데이터부터
# 삭제되는 것을 볼수있다.)

K = int(input())
stack_list = []
for i in range(K):
    num = int(input())
    if (num == 0):
        # 가장 최근에 쓴 수를 지우고,
        # (?)정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
        stack_list.pop()
    else:
        # 아닐 경우 해당 수를 쓴다.
        stack_list.append(num)
print(sum(stack_list))