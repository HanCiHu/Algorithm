import sys;
sys.setrecursionlimit(1000000)

S = input()
dp = [[0 for _ in range(len(S))] for _ in range(len(S))]
MOD = 10007

for i in range(len(S)): dp[i][i] = 1

def func(s, e):
  if dp[s][e]: return dp[s][e]
  if e < s: return 0
  dp[s][e] = (func(s + 1, e) + func(s, e - 1) - func(s + 1, e - 1)) % MOD
  if S[s] == S[e]: dp[s][e] = (dp[s][e] + func(s + 1, e - 1) + 1) % MOD
  return dp[s][e]

print(func(0, len(S) - 1))
