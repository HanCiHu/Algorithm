from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]
Times = [0 for _ in range(N + 1)]
q = deque()
for i in range(1, N + 1, 1):
  info = list(map(int, input().split(' ')))
  Times[i] = info[0]
  for j in range(1, len(info) - 1, 1):
    graph[info[j]].append(i)
    degree[i] += 1

for i in range(1, N + 1, 1):
  if degree[i] == 0:
    q.append(i)

ans = [0 for _ in range(N + 1)]

while q:
  node = q.popleft()
  ans[node] += Times[node]

  for i in graph[node]:
    degree[i] -= 1
    if degree[i] == 0: q.append(i)
    ans[i] = max(ans[i], ans[node])

print(ans)

