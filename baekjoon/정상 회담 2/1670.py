N = int(input())
dp = [0 for _ in range(10001)]

dp[0] = 1
dp[2] = 1
dp[4] = 2

for i in range(6, N + 1, 2):
  if i // 2 % 2 == 0: # 4, 8, 12 ...
    temp = 0
    for j in range(0, (i - 2) // 2, 2):
      temp += dp[j] * dp[i - j - 2]
    dp[i] = temp * 2

  else: # 6, 10, 14 ...
    temp = 0
    for j in range(0, (i - 2) // 2 - 1, 2):
      temp += dp[j] * dp[i - j - 2]
    dp[i] = temp * 2 + dp[(i - 2) // 2] * dp[(i - 2) // 2]

  dp[i] %= 987654321

print(dp[N] % 987654321)
