n = int(input())

INF = 300000

dp = [INF for _ in range(n + 1)]
dp[0] = 0
dp[1] = 0

for i in range(2, n + 1, 1):
  dp[i] = dp[i - 1] + 1
  if i % 2 == 0: dp[i] = min(dp[i // 2] + 1, dp[i])
  if i % 3 == 0: dp[i] = min(dp[i // 3] + 1, dp[i])
  if i % 5 == 0: dp[i] = min(dp[i // 5] + 1, dp[i])

print(dp[n])