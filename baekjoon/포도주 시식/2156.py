def func(i, flag):
  if (flag == 2):
    return func(i + 1, 0)
  if (i == n - 1):
    return cups[i]
  if (i >= n):
    return 0

  amount1 = cups[i] + func(i + 1, flag + 1)
  amount2 = func(i + 1, flag)

  return max(amount1, amount2)

n = int(input())
cups = [int(input()) for _ in range(n)]
print(func(0,0))
