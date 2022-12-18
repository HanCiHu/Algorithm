import sys
import heapq

sys.setrecursionlimit(999999)
INF = 999999999

def solution(n, paths, gates, summits):
  graph = [[] for _ in range(n + 1)]
  distance = [INF for _ in range(n + 1)]

  for [a, b, w] in paths:
    graph[a].append((b, w))
    graph[b].append((a, w))
  for g in gates: graph[0].append((g, 0))

  heap = [(0, 0)]

  while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist or now in summits: continue

    for n, d in graph[now]:
      new_dist = max(d, dist)
      if distance[n] > new_dist:
        distance[n] = new_dist
        heapq.heappush(heap, (new_dist, n))
  
  summit = dist = INF
  for g in summits:
    if dist > distance[g] or (dist == distance[g] and summit > g):
      summit = g
      dist = distance[g]


  return [summit, dist]

params = [(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]),
(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4]), (7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3,7], [1,5]),
(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1,2], [5]), (2, [[1,2,1]], [1], [2])]

for n, paths, gates, summits in params:
  print(solution(n, paths, gates, summits))
