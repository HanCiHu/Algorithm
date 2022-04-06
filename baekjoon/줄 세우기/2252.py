from collections import deque

N, M = map(int, input().split(' '))

graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for _ in range(M):
  s1, s2 = map(int, input().split(' '))
  graph[s1].append(s2)
  indegree[s2] += 1

q = deque()

for i in range(1, N + 1):
  if indegree[i] == 0:
    q.append(i)

while q:
  student = q.popleft()
  print(student, end=' ')

  for s in graph[student]:
    indegree[s] -= 1
    if indegree[s] == 0:
      q.append(s)
