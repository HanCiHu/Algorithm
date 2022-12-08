n = int(input())

storage = list(map(int, input().split(' ')))

def topDown(i, j):
  if i == n:
    return 0
  ans1 = 0
  ans2 = 0

  if j == 0: ans1 = storage[i] + topDown(i + 1, 1)
  ans2 = topDown(i + 1, 0)

  return max(ans1, ans2)

def bottomUp():
  dp = [0 for _ in range(n + 1)]
  dp[1] = storage[0]
  dp[2] = max(storage[1], storage[0])
  for i in range(3, n + 1, 1): dp[i] = max(dp[i - 2] + storage[i - 1], dp[i - 1])

  return dp[n]

print(topDown(0,0))
print(bottomUp())
