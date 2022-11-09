T = int(input())


dx = [0,0,1,-1, 1, 1, -1, -1]
dy = [1,-1,0,0, 1, -1, 1, -1]

def checkStone(nx, ny, s, i):
  while nx > 0 and ny > 0 and nx <= N and ny <= N:
    if board[ny][nx] == s: return True
    if board[ny][nx] == 0: return False
    nx += dx[i]
    ny += dy[i]
  return False

def changeStone(nx, ny, s, i):
  while board[ny][nx] != s:
    board[ny][nx] = s
    nx += dx[i]
    ny += dy[i]

def putStone(nx, ny, s):
  board[ny][nx] = s

for t in range(T):
  N, M = map(int, input().strip().split(' '))

  board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

  board[N//2 + 1][N//2] = 1
  board[N//2][N//2 + 1] =1
  board[N//2][N//2] = 2
  board[N//2 + 1][N//2 + 1] = 2

  for _ in range(M):
    x,y,s = map(int, input().strip().split(' '))
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      flag = checkStone(nx, ny, s, i)
      if flag:
        changeStone(nx, ny, s, i)
        putStone(x, y, s)

  w = 0
  b = 0

  for i in range(N + 1):
    for j in range(N + 1):
      if board[i][j] == 1: b += 1
      elif board[i][j] == 2: w += 1
  print('#', end='')
  print(t + 1, b,w)
