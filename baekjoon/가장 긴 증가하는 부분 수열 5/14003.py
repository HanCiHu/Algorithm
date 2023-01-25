from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split(' ')))
dp = [0 for _ in range(N)]

ans = 0
index = 0

tmp = [0]

for i in range(N):
  if tmp[-1] < arr[i]:
    tmp.append(arr[i])
    dp[i] = len(tmp) - 1
  else:
    find = bisect_left(tmp, arr[i])
    tmp[find] = arr[i]
    dp[i] = find
  if dp[i] > ans:
    ans = dp[i]
    index = i

LIS = [arr[index]]

cur = index
for i in range(index, -1, -1):
  if dp[cur] == dp[i] + 1:
    LIS.append(arr[i])
    cur = i

print(len(LIS))
for i in range(len(LIS)):
  print(LIS.pop(), end=' ')
