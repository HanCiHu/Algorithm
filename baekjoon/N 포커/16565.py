MOD = 10007

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

def combination(n, k):
    if k > n:
        return 0
    return (factorial(n) * pow(factorial(k) * factorial(n - k), -1, MOD)) % MOD

n = int(input())

dp = [[0 for _ in range(53)] for _ in range(53)]
dp[0][0] = 1

for i in range(1, 53):
  for j in range(i + 1):
    if j == 0 or j == i + 1:
      dp[i][j] = 1
    else:
      dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

ans = 0

for i in range(1, n // 4 + 1):
  if i % 2 == 0: ans = (ans - (dp[13][i] * dp[52 - 4 * i][n - 4 * i]) % MOD + MOD) % MOD
  else: ans = (ans + dp[13][i] * dp[52 - 4 * i][n - 4 * i]) % MOD

print(ans)
