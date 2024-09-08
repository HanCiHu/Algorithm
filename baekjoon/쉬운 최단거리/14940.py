from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = [[0 for _ in range(M)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque([])

for y in range(N):
  for x in range(M):
    if board[y][x] == 2:
      q.append((x, y, 0))

while q:
  x,y,n = q.popleft()

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]

    if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1 and answer[ny][nx] == 0:
      q.append((nx, ny, n + 1))
      answer[ny][nx] = n + 1

for y in range(N):
  for x in range(M):
    if board[y][x] == 1 and answer[y][x] == 0:
      answer[y][x] = -1

for i in answer:
  for j in i:
    print(j, end=' ')
  print()
