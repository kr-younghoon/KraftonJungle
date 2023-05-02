# Q13(1946) - 신입 사원 | 출력 4\n3
'''
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
'''

T = int(input()) # 2

for _ in range(T): # 2times run
    N = int(input()) # 5
    rank = [list(map(int, input().split())) for _ in range(N)] # [[3, 2], [1, 4], [4, 1], [2, 3], [5, 5]]
    sorted_rank = sorted(rank) # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    top = 0 # 끝자리 수 비교를 위한 top 변수 선언
    result = 1 # 최대인원 수 카운트를 위한 result 변수 선언
    for i in range(1, len(sorted_rank)): # len(sorted_rank) = 5  |  4times run (1-4)
        if sorted_rank[i][1] < sorted_rank[top][1]: # 각 항의 [1]인덱스와 TOP변수 그니까 시간을 쓰고 있는 변수가 저장되어 넘어가야함.
            top = i #
            result += 1 
            
    print(result)