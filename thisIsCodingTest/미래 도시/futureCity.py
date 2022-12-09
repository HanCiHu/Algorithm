import heapq

N,M = map(int, input().split(' '))
graph = [[] for _ in range(N + 1)]
INF = 1000


for _ in range(M):
  start,end = map(int, input().split(' '))  
  graph[start].append((1, end))
  graph[end].append((1, start))

X, K = map(int, input().split(' '))
def dij(start, end):  
  distance = [INF for _ in range(N + 1)]
  distance[start] = 0
  hq = [(0,start)]

  while hq:
    dist, now = heapq.heappop(hq)

    if dist > distance[now]: continue

    for i in graph[now]:
      cost = dist + i[0]
      if cost < distance[i[1]]:
        distance[i[1]] = cost
        heapq.heappush(hq, (cost, i[1]))
  return distance[end]

ans = dij(1, K) + dij(K,X)

print(-1 if ans >= INF else ans)