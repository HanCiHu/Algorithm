import sys; input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
arr = list(map(int ,input().split()))

ans = []
comb = []

for i in range(N - 1):
  for j in range(i+1, N):
    if i == j: continue
    comb.append((arr[i] + arr[j], i,j))
comb.sort()

p1, p2 = 0,1

while p1 < p2 and p1 < len(comb) - 1:
  if comb[p1][1] in comb[p2][1:] or comb[p1][2] in comb[p2][1:]:
    p2 += 1
    if p2 == len(comb):
      p1 += 1
      p2 = p1 + 1
    continue
  else:
    ans.append(abs(comb[p2][0] - comb[p1][0]))
    p1 += 1
    p2 = p1 + 1

print(min(ans))