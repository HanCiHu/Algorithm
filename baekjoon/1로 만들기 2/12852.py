n = int(input())

dp = [[] for _ in range(n + 1)]
dp[1] = [1]
if n > 1:
  dp[2] = [1, 2]
if n > 2:
  dp[3] = [1, 3]

for i in range(4, n + 1, 1):
  if i % 3 == 0 and i % 2 == 0:
    dp[i] = dp[i//2] + [i] if len(dp[i // 2]) < len(dp[i // 3]) else dp[i//3] + [i]
  elif i % 3 == 0:
    dp[i] = dp[i // 3] + [i] if len(dp[i // 3]) < len(dp[i - 1]) else dp[i - 1] + [i]
  elif i % 2 == 0:
    dp[i] = dp[i // 2] + [i] if len(dp[i // 2]) < len(dp[i - 1]) else dp[i - 1] + [i]
  else:
    dp[i] = dp[i - 1] + [i]

print(len(dp[n]) - 1)
for i in range(len(dp[n]) - 1, -1, -1):
  print(dp[n][i], end=" ")