# Q1904 - 01타일
'''
예제 입력 1 : 4 / 예제 출력 1 : 5

출력
첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.
'''

# 실패 | 메모리 초과

import sys
input = sys.stdin.readline

N = int(input())
tile = [1, 2]
for i in range(2, N):
    tile.append(tile[i-1] + tile[i-2])
print(tile[N-1] % 15746)

# tile.append(tile[i-1] + tile[i-2]) 로만 저장하면 큰수가 저장되어서 메모리 초과


# 성공
import sys
input = sys.stdin.readline

N = int(input())
tile = [1, 2]
for i in range(2, N):
    tile.append((tile[i-1] + tile[i-2]) % 15746)
print(tile[N-1])


# 이 둘 차이가 뭡니까?
# 난 나누기 밖에 안옮겼는데