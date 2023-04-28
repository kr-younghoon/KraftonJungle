N = int(input())

# 초기값 설정
dp = [0, 1, 2]

# 동적 계획법을 이용하여 문제 해결
for i in range(3, N+1):
    dp.append((dp[i-1] + dp[i-2]) % 15746)

print(dp[N])
