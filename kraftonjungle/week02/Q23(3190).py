# input 모듈 입력
import sys
input = sys.stdin.readline

N = int(input()) # 보드의 크기 N
K = int(input()) # 사과 위치의 대한 명령 갯수 K
L = int(input()) # 정수 X와 문자 C를 입력하는 for문의 횟수 L
L_list = K_list = []

for i in range(K):
    K_list.append(list(map(int, input().split())))

for j in range(L):
    L_list.append(list(map(int, input().split())))

for k in range(1, N + 1):
    for l in range(1, N + 1):
        