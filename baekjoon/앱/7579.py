

N, M = map(int, input().split(' '))

mem = [0] + list(map(int, input().split(' ')))
cost = [0] + list(map(int, input().split(' ')))

s = sum(cost) + 1
dp = [[0 for _ in range(s)] for _ in range(N + 1)]


for i in range(1, N + 1):
  for j in range(s):
    if cost[i] <= j:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + mem[i])
    else:
      dp[i][j] = dp[i - 1][j]

ans = float('inf')

for i in range(1, len(dp)):
  for j in range(1, len(dp[i])):
    if dp[i][j] >= M:
      ans = min(ans, j)
print(ans)
