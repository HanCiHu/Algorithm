n = int(input())

juice = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

dp[0] = juice[0]
if n > 1: dp[1] = juice[0] + juice[1]
if n > 2 : dp[2] = max(juice[0] + juice[2], juice[1] + juice[2], dp[1])

for i in range(3, n):
  dp[i] = max(juice[i] + juice[i - 1] + dp[i - 3], juice[i] + dp[i - 2] , dp[i - 1])

print(dp[n - 1])