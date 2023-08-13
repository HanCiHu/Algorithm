s = input()
N = len(s)
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
  for j in range(N):
    if s[i] != ')': dp[i + 1][j + 1] = (dp[i][j] + dp[i + 1][j + 1]) % 998244353
    if s[i] != '(' and j != 0: dp[i + 1][j - 1] = (dp[i][j] + dp[i + 1][j - 1]) % 998244353

print(dp[N][0] % 998244353)