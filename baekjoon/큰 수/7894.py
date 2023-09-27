import sys;input=sys.stdin.readline
import math

N = int(input())

for _ in range(N):
  M = int(input())
  num = 0
  for i in range(1, M + 1, 1): num += math.log10(i)
  print(math.floor(num) + 1)
