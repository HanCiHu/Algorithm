from heapq import heappop, heappush

N, M = map(int, input().split(' '))

graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split(' '))
  graph[a].append(b)
  indegree[b] += 1

q = []

for i in range(1, N + 1):
  if indegree[i] == 0:
    heappush(q, i)

while q:
  problem = heappop(q)

  print(problem, end=' ')

  for p in graph[problem]:
    indegree[p] -= 1
    if indegree[p] == 0:
      heappush(q, p)


