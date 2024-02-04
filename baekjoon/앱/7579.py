N, M = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(N + 1)]

ans = sum(cost)

for i in range(1, N + 1):
  for j in range(0, sum(cost) + 1):
    if j < cost[i]: dp[i][j] = dp[i - 1][j]
    else: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + mem[i])
    if dp[i][j] >= M: ans = min(ans, j)

if M != 0: print(ans)
else: print(0)
