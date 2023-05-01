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

T = int(input())

for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    sorted_rank = sorted(rank)
    top = 0
    result = 1
    for i in range(1, len(sorted_rank)):
        if sorted_rank[i][1] < sorted_rank[top][1]:
            top = i
            result += 1
            
    print(result)