N, M = map(int, input().split(' '))

parents = [i for i in range(N + 1)]

for i in range(M):
  start, end = map(int, input().split(' '))
  parents[end] = start

answer = []

for i in range(1, N + 1, 1):
  if i == parents[i]: answer.append(i)

print(answer[0] if len(answer) == 1 else -1)
