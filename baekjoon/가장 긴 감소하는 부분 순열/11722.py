N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]

for i in range(N):
  for j in range(i):
    if arr[i] < arr[j] and dp[i] < dp[j]: dp[i] = dp[j]
  dp[i] += 1

print(max(dp))