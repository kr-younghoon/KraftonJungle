# Q9084 - 동전
'''
3
2
1 2
1000
3
1 5 10
100
2
5 7
22
'''
#입력!
#입력의 첫줄 테스트 개수(T)
#각 테스트 케이스의 첫번째 줄에는 동전의 가지 수 N
#둘째 줄 N가지 동전의 각 금액이 오름차순으로 정렬되어 주어진다.
#세번째 줄에는 주어진 N가지 동전으로 만들어야 할 금액 M이 주어진다.
#출력
# 각테스트 케이스 에 대해 입력으로 주어지는 N가지 동전으로 금액 M을 만드는 모든 방법의 수를 한줄에 하나씩 출력한다.

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    required_amount = int(input())

    table = [0] * (required_amount + 1)
    table[0] = 1

    for coin in coins:
        for i in range(required_amount + 1):
            if i >= coin:
                table[i] += table[i - coin]
    print(table[required_amount])