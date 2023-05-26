from heapq import heappop, heappush
import sys
input = sys.stdin.readline

num = int(input())
cards = []
for i in range(num):
    heappush(cards, int(input()))

answer = 0
    
while len(cards) > 1:    
    x = heappop(cards)
    y = heappop(cards)
    answer += x + y
    heappush(cards, x + y)

print(answer)