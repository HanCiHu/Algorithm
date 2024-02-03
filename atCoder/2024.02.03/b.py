dx = [1,0,-1,0]
dy = [0,1,0,-1]

H, W, N = map(int, input().split())
board = [['.' for _ in range(W)] for _ in range(H)]

i = -1
x, y = 0,0
for _ in range(N):
  board[y][x] = '.' if board[y][x] == '#' else '#'
  if board[y][x] == '#':
    i += 1
    i %= 4
  else: i -= 1
  x += dx[i]
  x %= W
  y += dy[i]
  y %= H

for k in board: print(''.join(k))