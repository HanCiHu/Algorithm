N = int(input())
b = list(map(int, input().split(' ')))
lights = list(map(int, input().split(' ')))

points = 0

for i in range(N):
  if lights[i] == 1:
    points += b[i]

dp = [float('-inf') for _ in range(N + 1)]

for i in range(N):
  k = b[i] if lights[i] == 0 else -b[i]
  dp[i] = max(dp[i - 1] + k, k)

print(points + max(dp))