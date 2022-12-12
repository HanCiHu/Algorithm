import heapq
import math

N = int(input())

starts = [list(map(lambda x: int(float(x) * 100), input().split(' '))) for _ in range(N)]
parents = [i for i in range(N + 1)]

def find(x):
  if parents[x] != x: parents[x] = find(parents[x])
  return parents[x]

def union(x,y):
  x = find(x)
  y = find(y)

  if x < y: parents[y] = x
  else: parents[x] = y

heap = []

for i in range(N - 1):
  for j in range(i + 1, N, 1):
    heapq.heappush(heap, (math.pow(math.pow(starts[i][0] - starts[j][0], 2) + math.pow(starts[i][1] - starts[j][1], 2), 0.5), i, j))

result = 0

while heap:
  dist, start, end = heapq.heappop(heap)
  if find(start) != find(end):
    union(start, end)
    result += dist

print(round(result / 100, 2))

