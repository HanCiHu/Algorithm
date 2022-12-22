import sys
from functools import reduce

input = sys.stdin.readline

N,M,B = map(int, input().split(' '))
ground = [list(map(int, input().split(' '))) for _ in range(N)]

n,m = 0,300

ans = 999999999
high = 0

for i in range(257):
  b = 0
  time = 0
  for j in ground:
    for k in j:
      if k > i:
        b += k - i
        time += (k - i) * 2
      else:
        b -= i - k
        time += (i - k)

  if B + b >= 0:
    if ans > time or (ans == time and i > high):
      ans = time
      high = i

print(ans, high)
