from collections import deque

N, M = map(int, input().split(' '))

songs = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]
result = []

for _ in range(M):
  order = list(map(int, input().split(' ')))

  for i in range(1, len(order) - 1):
    songs[order[i]].append(order[i + 1])
    degree[order[i + 1]] += 1

q = deque()
for i in range(1, N + 1, 1):
  if degree[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  result.append(now)

  for i in songs[now]:
    degree[i] -= 1
    if degree[i] == 0:
      q.append(i)

if sum(degree) > 0: print(0)
else:
  for i in result:
    print(i)