N,M = map(int, input().split(' '))
moneys = [int(input()) for _ in range(N)]

INF = 999999999

dp = [INF for _ in range(M + 1)]

for m in moneys:
  if m <= M:
    dp[m] = 1

for i in range(1, M + 1, 1):
  for j in moneys:
    if j < i: dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[M] if dp[M] != INF else -1)
