import math
import heapq

N,M = map(int, input().split())

location = [list(map(int, input().split())) for _ in range(N)]
connect = [list(map(int, input().split())) for _ in range(M)]

INF = float('inf')

graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
  for j in range(N):
    distance = math.sqrt(((location[i][0] - location[j][0]) ** 2 + (location[i][1] - location[j][1]) ** 2))
    graph[i][j] = distance
    graph[j][i] = distance

for i in range(M):
  [start,end] = connect[i]
  graph[start - 1][end - 1] = 0
  graph[end - 1][start - 1] = 0

selected = [False for _ in range(N)]

q = [(0,0)]

ans = 0

while q:
  w,v = heapq.heappop(q)
  if not selected[v] and w != INF:
    selected[v] = True
    ans += w
    
    for i in range(N):
      if i != v and not selected[i] and graph[v][i] != INF:
        heapq.heappush(q, (graph[v][i], i))

print(format(ans,'.2f'))