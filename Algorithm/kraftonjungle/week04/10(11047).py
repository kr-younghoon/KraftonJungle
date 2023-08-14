# 10번(Q11047) - 동전 0 / 그리디 / 앞선 선택이 뒤에 영향을 주면 안된다.

N, K = map(int, input().split())
variety = []
for _ in range(N):
    variety.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K // variety[i]
    K = K % variety[i]

print(count)