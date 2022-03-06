INF = float('INF')
N, M = map(int, input().split(' '))

graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
  start, end, value = map(int, input().split(' '))
  graph[start].append((value, end))

def bell_ford():
  distance[1] = 0
  for i in range(N):
    for j in range(1, N + 1, 1):
      for value, vertex in graph[j]:
        if distance[vertex] > value + distance[j]:
          distance[vertex] = value + distance[j]
          if i == N - 1:
            return True
  return False

if bell_ford():
  print(-1)
else:
  for i in range(2, len(distance)):
    print(distance[i]) if distance[i] != INF else print(-1)
