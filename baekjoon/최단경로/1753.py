import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

class node:
  def __init__(self, v, w):
    self.v = v
    self.w = w

  def __lt__(self, other):
    return self.v < other.w # 오름차순

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
  heapq.heappush(heap, node(start, 0))

  while heap:
    n = heapq.heappop(heap)

    vertex, weight = n.v, n.w

    if (distance[vertex] < weight): continue

    for v, w in graph[vertex]:
       if distance[v] > weight + w:
         distance[v] = weight + w
         heapq.heappush(heap, node(v, weight + w))

  for i in range(1, V+1):
    print(distance[i]) if distance[i] != INF else print('INF')

dijkstra(K)