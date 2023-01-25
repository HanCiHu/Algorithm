from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split(' ')))
dp = [0 for _ in range(N)]
dp[0] = 1

ans = 0
index = 0

for i in range(1, N, 1):
  for j in range(i):
    if arr[j] < arr[i] and dp[i] < dp[j]:
      dp[i] = dp[j]
  dp[i] += 1
  if ans < dp[i]:
    index = i
    ans = dp[i]

LIS = [arr[index]]

cur = index
for i in range(index, -1, -1):
  if dp[cur] == dp[i] + 1:
    LIS.append(arr[i])
    cur = i

print(len(LIS))
for i in range(len(LIS)):
  print(LIS.pop(), end=' ')
