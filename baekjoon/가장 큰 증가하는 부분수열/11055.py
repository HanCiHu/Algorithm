N = int(input())
arr = list(map(int, input().split()))

dp = [0 for i in range(N)]

for i in range(N):
  for j in range(i):
    if arr[i] > arr[j] and dp[j] > dp[i]: dp[i] = dp[j]
  dp[i] += arr[i]

print(max(dp))