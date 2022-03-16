from collections import deque
n = int(input())

graph = [[] for _ in range(n + 1)]
cost = [0 for _ in range(n + 1)]
indegree = [ 0 for _ in range(n+1)]
answer = [0 for _ in range(n + 1)]

for i in range(1, n + 1, 1):
  lst = list(map(int, input().split(' ')))
  cost[i] = lst[0]
  for j in range(1, len(lst) - 1):
    graph[lst[j]].append(i)
    indegree[i] += 1

q = deque()

for i in range(1, n + 1, 1):
  if indegree[i] == 0:
    q.append(i)

while q:
  node = q.popleft()

  answer[node] += cost[node]

  for n in graph[node]:
    indegree[n] -= 1
    answer[n] = max(answer[n], answer[node])
    if indegree[n] == 0:
      q.append(n)

for i in answer[1:]:
  print(i, end=' ')
