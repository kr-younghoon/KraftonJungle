# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다.

# 예제 생략 (count = 4, words = but i wont hesitate)로 임시사용


import sys
input = sys.stdin.readline

n = int(input())
word_list = []

for i in range(n):
    word_list.append(input().strip())

set_list = set(word_list) # 중복된 단어들 삭제
word_list = list(set_list) # set 함수로 set 객체를 다시 리스트로 변환해야한다.
word_list.sort() # 알파벳 순서대로 정렬한다.
word_list.sort(key = len) # 단어의 길이를 기준으로 한번 더 정렬하였다.

for i in word_list:
    print(i)