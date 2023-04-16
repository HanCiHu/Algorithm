from collections import deque
from copy import deepcopy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split(' ')) # N세로, M가로
answer = 0
board = [list(map(int, input().split(' '))) for _ in  range(N)]
wall = []
virus = deque([])
for i in range(N):
  for j in range(M):
    if board[i][j] == 2:
      virus.append((j,i))

def func(wall, board):
  global answer
  if len(wall) < 3:
    for i in range(N):
      for j in range(M):
        if board[i][j] == 0:
          board[i][j] = 1
          wall.append((j,i))
          func(wall, deepcopy(board))
          board[i][j] = 0
          wall.pop()
    return
  q = deque([])
  for i in virus: q.append(i)

  while q:
    x,y = q.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx >= 0 and nx < M and ny >= 0 and ny < N and board[ny][nx] == 0:
        board[ny][nx] = 2
        q.append((nx,ny))

  safe = 0
  for i in range(N):
    for j in range(M):
      if board[i][j] == 0:
        safe += 1
        answer = max(answer, safe)


func(wall, board)

print(answer)