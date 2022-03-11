T = int(input())

for _ in range(T):
  n = int(input())
  tri = [list(map(int, input().strip().split(' '))) for _ in range(n)]
  cost = [[0 for _ in range(i + 1)] for i in range(n)]
  cnt = [[0 for _ in range(i + 1)] for i in range(n)]

  cost[0][0] = tri[0][0]
  cnt[0][0] = 1

  for i in range(1, n):
    for j in range(i + 1):
      if j == 0:
        cost[i][j] = tri[i][j] + cost[i - 1][j]
        cnt[i][j] = cnt[i - 1][j]
      elif j == i:
        cost[i][j] = tri[i][j] + cost[i - 1][j - 1]
        cnt[i][j] = cnt[i - 1][j - 1]
      else:
        if cost[i - 1][j - 1] > cost[i - 1][j]:
          cost[i][j] = cost[i - 1][j - 1] + tri[i][j]
          cnt[i][j] = cnt[i - 1][j - 1]
        elif cost[i - 1][j - 1] < cost[i - 1][j]:
          cost[i][j] = cost[i - 1][j] + tri[i][j]
          cnt[i][j] = cnt[i - 1][j]
        else:
          cost[i][j] = cost[i - 1][j] + tri[i][j]
          cnt[i][j] = cnt[i - 1][j] + cnt[i - 1][j - 1]
  max_val = max(cost[n - 1])
  ans = 0

  for i in range(n):
    if cost[n - 1][i] == max_val:
      ans += cnt[n - 1][i]
  print(ans)
