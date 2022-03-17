N, M = map(int, input().split(' '))

dp = [0 for _ in range(M + 1)]
objects = []

for _ in range(N):
  W, C, K = map(int, input().split(' '))

  i = 1
  while K > 0:
    m = min(i, K)
    objects.append((W * m, C * m))
    K -= i
    i *= 2

for W, C in objects:
  for i in range(M, W - 1, -1):
    dp[i] = max(dp[i], dp[i - W] + C)

print(dp[M])
