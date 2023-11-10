import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))
  reverse_graph[end].append((start, cost))

INF = float('inf')

distance_from_X = [INF for _ in range(N + 1)]
distance_from_X[X] = 0
q = [(0, X)]

while q:
  cost, node = heapq.heappop(q)
  if cost > distance_from_X[node]: continue

  for n, c in graph[node]:
    if cost + c < distance_from_X[n]:
      heapq.heappush(q, (cost + c, n))
      distance_from_X[n] = cost + c

distance = [INF for _ in range(N + 1)]
distance[X] = 0

q = [(0, X)]

while q:
  cost, node = heapq.heappop(q)
  if cost > distance[node]: continue

  for n, c in reverse_graph[node]:
    if cost + c < distance[n]:
      heapq.heappush(q, (cost + c, n))
      distance[n] = cost + c

print(max([distance[i] + distance_from_X[i] for i in range(1, N + 1, 1)]))