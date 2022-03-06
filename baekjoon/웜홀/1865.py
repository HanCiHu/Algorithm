T = int(input())
INF = 2147483647

def bell_ford(distance, graph, N):
  for i in range(N):
    for j in range(1, N + 1, 1):
      for vertex, value in graph[j]:
        if distance[vertex] > distance[j] + value:
          distance[vertex] = distance[j] + value
          if i == N - 1:
            return True
  return False

for _ in range(T):
  N,M,W = map(int, input().split(' '))
  distance = [INF for _ in range(N + 1)]
  graph = [[] for _ in range(N + 1)]

  for _ in range(M):
    S, E, V = map(int, input().split(' '))
    graph[S].append((E, V))
    graph[E].append((S, V))

  for _ in range(W):
    S, E, V = map(int, input().split(' '))
    graph[S].append((E, -V))

  print("YES") if bell_ford(distance, graph, N) else print("NO")
