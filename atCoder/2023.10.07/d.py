from collections import defaultdict
import sys; input=sys.stdin.readline

N = int(input())
slimes = defaultdict(int)

for _ in range(N):
  size, cnt = map(int, input().split())
  while size % 2 == 0:
    size //= 2
    cnt *= 2
  slimes[size] += cnt

ans = 0

for i in slimes:
  cnt = slimes[i]

  while cnt > 0:
    if cnt % 2 == 1: ans += 1
    cnt //= 2

print(ans)
