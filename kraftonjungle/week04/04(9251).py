# LCS - Q9251
'''
예제 입력 1 :
ACAYKP
CAPCAK
예제 출력 1 :
4
'''
# import sys
# read = sys.stdin.readline

# word1, word2 = read().strip(), read().strip()
# h, w = len(word1), len(word2)
# cache = [[0] * (w+1) for _ in range(h+1)]

# for i in range(1, h+1):
#     for j in range(1, w+1):
#         if word1[i-1] == word2[j-1]:
#             cache[i][j] = cache[i-1][j-1] + 1
#         else:
#             cache[i][j] = max(cache[i][j-1], cache[i-1][j])
# print(cache[-1][-1])

import sys
input = sys.stdin.readline

word1, word2 = input().strip(), input().strip()
h, w = len(word1), len(word2)
cache = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if word1[i - 1] == word2[j - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])
            
print(cache[-1][-1])