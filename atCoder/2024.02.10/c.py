from collections import defaultdict

N = int(input())
dp = defaultdict(int)

ans = 0
dp[2] = 2
dp[3] = 5

def func(n):
  if dp[n] > 0: return dp[n]
  if n == 1: return 0
  if n == 2: return 2
  if n == 3: return 5

  if n % 2 == 1:
    dp[n] = n // 2 + n // 2 + 1 + func(n // 2) + func(n // 2 + 1)
  else:
    dp[n] += n +  2 * func(n // 2)
  
  return dp[n]

print(func(N))
