from collections import deque

INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

cap = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
flow = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
  s,e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)
  cap[s][e] = 1

def netflow(source, sink):
  t = 0

  while True:
    path = [-1 for _ in range(N + 1)]
    q = deque([source])

    while q and path[sink] == -1:
      here = q.popleft()
      for there in graph[here]:
        if cap[here][there] - flow[here][there] > 0 and path[there] == -1:
          q.append(there)
          path[there] = here

    if path[sink] == -1: break

    amount = INF
    p = sink
    while p != source:
      amount = min(cap[path[p]][p] - flow[path[p]][p], amount)
      p = path[p]
    
    p = sink
    while p != source:
      flow[path[p]][p] += amount
      flow[p][path[p]] -= amount
      p = path[p]

    t += amount
  return t

print(netflow(1, 2))
