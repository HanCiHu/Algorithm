import sys; input = sys.stdin.readline
from itertools import combinations
from bisect import bisect_left, bisect_right

N, target = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

left = arr[:N//2]
right = arr[N//2:]

leftSum, rightSum = [], []

for i in range(1, N//2 + 2, 1):
  for j in combinations(right, i):
    rightSum.append(sum(j))
  if len(left) < i: continue
  for j in combinations(left, i):
    leftSum.append(sum(j))

leftSum.sort()
rightSum.sort()

ans = 0

for i in leftSum:
  ans += bisect_right(rightSum, target - i) - bisect_left(rightSum, target - i)
  if i == target: ans += 1

ans += bisect_right(rightSum, target) - bisect_left(rightSum, target)

print(ans)