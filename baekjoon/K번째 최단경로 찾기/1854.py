import heapq

N,M,K = map(int, input().split())
INF = float('inf')

graph = [[] for _ in range(N + 1)]
distance = [[-INF for _ in range(K)] for _ in range(N + 1)]
heapq.heappush(distance[1], 0)
heapq.heappop(distance[1])

for _ in range(M):
  start, end, cost = map(int, input().split(' '))
  graph[start].append((end, cost))

q = [(0, 1)]

while q:
  dist, node = heapq.heappop(q)

  for n, c in graph[node]:
    if dist + c < -(distance[n][0]):
      heapq.heappush(q, (dist + c, n))
      heapq.heappush(distance[n], -(dist + c))
      heapq.heappop(distance[n])

for i in range(1, N + 1, 1):
  print(-distance[i][0]) if -distance[i][0] != INF else print(-1)