from collections import defaultdict
N, M, K = map(int, input().split(' '))

plants = list(map(int, input().split(' ')))
plant_map = defaultdict(lambda: False)
for p in plants:
  plant_map[p] = True
graph = [list(map(int, input().split(' '))) for _ in range(M)]
parents = [j for j in range(N + 1)]

graph.sort(key=lambda x: x[2])

def find(x):
  global parents
  if parents[x] != x: parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  x, y = find(x), find(y)

  if plant_map[x]: parents[y] = x
  elif plant_map[y]: parents[x] = y
  elif x < y: parents[y] = x
  else: parents[x] = y

cost = 0


for [u,v,w] in graph:
  u,v = find(u), find(v)
  if find(u) != find(v) and not (plant_map[u] and plant_map[v]):
    union(u, v)
    cost += w

print(cost)