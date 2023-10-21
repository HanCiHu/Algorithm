N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(24):
  tmp = 0
  for [cnt, time] in arr:
    t = (i + time) % 24
    if 9 <= t < 18: tmp += cnt
  ans = max(ans, tmp)
print(ans)