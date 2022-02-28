import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, input().split(' '))
K = int(input())

graph = [[] for _ in range(V + 1)]

for i in range(E):
  u,v,w = map(int, input().split(' '))
  graph[u].append((v, w))

def dijkstra(start):
  heap = []
  distance = [INF] * (V + 1)

  distance[start] = 0
  heapq.heappush(heap, (0, start))

  while heap:
    weight, vertex = heapq.heappop(heap)

    if weight > distance[vertex]: continue

    for v, w in graph[vertex]:
       if distance[v] > weight + w:
         distance[v] = weight + w
         heapq.heappush(heap, (weight + w, v))

  for i in range(1, V+1):
    print(distance[i]) if distance[i] != INF else print('INF')

dijkstra(K)