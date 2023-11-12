N, M = map(int, input().split())
S = input()

chars = list(set(S))

dp = [0 for _ in range(N + 1)]
subsum = [0 for _ in range(N + 1)]

for i in range(1, N):
  if S[i] == S[i - 1]: dp[i] += 1
for i in range(1, N):
  subsum[i] += subsum[i - 1] + dp[i]

for _ in range(M):
  start, end = map(int, input().split())
  print(subsum[end - 1] - subsum[start - 1])

