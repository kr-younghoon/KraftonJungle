#콥셈 - IN / "10 11 12" OUT / "4"

# Q : 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 
# 이를 C로 나눈 나머지를 구하는 프로그램을 작성하라.

# IN : 첫째 줄에 A, B, C가 빈칸을 사이에 두고 순서대로 주어진다. 
# A, B, C는 모두 2,147,483,647 이하의 자연수이다.
# OUT : 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def hello(N, k, d):
    if k == 0:
        return 1
    elif k == 1:
        return N % d
    
    tmp = hello(N, k//2, d)
    if k % 2:
        return (tmp * tmp * N) % d
    else:
        return (tmp * tmp) % d
    
print(hello(A, B, C))

'''
공-식 무조건 외워야 함
__________________

N^k에 대해,

k가 홀수이면 N^(k//2) N^(k//2) N

k가 짝수이면 N^(k//2) * N^(k//2) 로 분할해서 계산한다
'''