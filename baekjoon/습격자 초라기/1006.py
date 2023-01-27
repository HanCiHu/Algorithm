import sys; input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

T = int(input())

region1=[]; region2=[]; dp=[]
N=0;W=0

def func(i, flag1, flag2, first1, first2):
  if i == N: return 0

  if dp[i][flag1][flag2][first1][first2] > -1:
    return dp[i][flag1][flag2][first1][first2]

  ans = func(i + 1, False, False, first1, first2)

  if N > 1:
    if (region1[i] + region1[i - 1] <= W and not flag1) and (region2[i] + region2[i - 1] <= W and not flag2):
      if i == N - 1 and not first1 and not first2:
        ans = max(ans, 2 + func(i + 1, True, True, True, True))
      elif i == 0:
        ans = max(ans, 2 + func(i + 1, True, True, True, True))
      elif i != N - 1:
        ans = max(ans, 2 + func(i + 1, True, True, first1, first2))

    if region1[i] + region1[i - 1] <= W and not flag1:
      if i == N - 1 and not first1:
        ans = max(ans, 1 + func(i + 1, True, False, True, first2))
      elif i == 0:
        ans = max(ans, 1 + func(i + 1, True, False, True, first2))
      elif i != N - 1:
        ans = max(ans, 1 + func(i + 1, True, False, first1, first2))

    if region2[i] + region2[i - 1] <= W and not flag2:
      if i == N - 1 and not first2:
        ans = max(ans, 1 + func(i + 1, False, True, first1, True))
      elif i == 0:
        ans = max(ans, 1 + func(i + 1, False, True, first1, True))
      elif i != N - 1:
        ans = max(ans, 1 + func(i + 1, False, True, first1, first2))

  if region1[i] + region2[i] <= W:
      if i == N - 1 and not first1 and not first2:
        ans = max(ans, 1 + func(i + 1, True, True, first1, first2))
      elif i != N - 1:
        ans = max(ans, 1 + func(i + 1, True, True, first1, first2))

  dp[i][flag1][flag2][first1][first2] = ans
  return dp[i][flag1][flag2][first1][first2]

for _ in range(T):
  N, W = map(int, input().split(' '))
  region1 = list(map(int, input().split(' ')))
  region2 = list(map(int, input().split(' ')))
  dp = [[[[[-1,-1], [-1,-1]], [[-1,-1], [-1,-1]]], [[[-1,-1], [-1,-1]], [[-1,-1], [-1,-1]]]] for _ in range(N)]
  print(2 * N - func(0, False, False, False, False))
