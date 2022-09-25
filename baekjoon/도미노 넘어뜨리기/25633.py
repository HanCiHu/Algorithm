N = int(input())
M = list(map(int, input().split(' ')))

dp = [1 for _ in range(N + 1)]

for i in range(N):
  weight = M[i]
  cnt = 1
  for j in range(i + 1, N, 1):
    if weight >= M[j]:
      weight += M[j]
      cnt += 1
      dp[j] = max(dp[j], cnt)

print(max(dp))