# 문제 : 산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 
# 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오

# -------------------------------------------------------------------------------------- #
import sys
input = sys.stdin.readline

# 두 용액 (Q2470)

# 입력 : 첫째 줄에는 전체 용액의 수 N이 입력된다. 
# N은 2 이상 100,000 이하이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 
# 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 다르고, 
# 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

# 예제 input 1
# 5
# -2 4 -99 -1 98

import sys
input = sys.stdin.readline

N = int(input())
solution_list = list(map(int, input().split()))
solution_list.sort()

left, right = 0, N - 1
total = float('inf')
min_left = min_right = 0

while(left < right):
    m = solution_list[left] + solution_list[right]
    
    if abs(m) < abs(total):
        total = m
        min_left, min_right = solution_list[left], solution_list[right]
        
    if m == 0:
        break
    elif m < 0:
        left += 1
    else:
        right -= 1        

print(min_left, min_right)

# 출력 : 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 
# 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 
# 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.

# 예제 output 1
# -99 98

#total에 대한 float('inf')사용
# float('inf')는 양의 무한대이다. -inf를 사용하면 음의 무한대가 된다.

