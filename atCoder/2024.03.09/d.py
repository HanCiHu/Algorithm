target = input()
N = int(input())
bags = [list(map(str, input().split()))[1:] for _ in range(N)]

INF = 2100000000

dp = [[0 for _ in range(101)] for _ in range(101)]

def func(i, j):
  if j == len(target): return 0
  if i == N: return INF
  if dp[i][j] > 0: return dp[i][j]

  ans = func(i + 1, j)

  for s in bags[i]:
    if target[j: j + len(s)] == s:
      ans = min(ans, 1 + func(i + 1, j + len(s)))
  dp[i][j] = ans

  return ans

ans = func(0,0)

print(ans if ans != INF else -1)