from collections import defaultdict

N = int(input())

well = [int(input()) for _ in range(N)]
water = defaultdict(int)
edges = [list(map(int, input().split(' '))) for _ in range(N)]
sorted_edges = []

parents = [i for i in range(N + 1)]

for i in range(N):
  for j in range(i+1, N, 1):
    if edges[i][j] > 0:
      sorted_edges.append((edges[i][j], i, j))

for i in range(N): sorted_edges.append((well[i], i, N))

sorted_edges.sort(key= lambda x: x[0])

def find(x):
  if parents[x] != x: parents[x]= find(parents[x])
  return parents[x]

def union(x,y):
  x = find(x)
  y = find(y)
  
  if x <= y: parents[y] = x
  else: parents[x] = y

answer = 0

for w,s,e in (sorted_edges):
  if find(s) != find(e):
    union(s,e)
    answer += w

print(answer)
