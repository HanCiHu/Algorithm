N = int(input())

t_dx = [[0,-1,0,1,-2,-1,-1,0,1,0], [-2,-1,-1,-1,0,0,1,1,1,2], [0,1,0,-1,2,1,1,0,-1,0], [-2,-1,-1,-1,0,0,1,1,1,2]]
t_dy = [[-2,-1,-1,-1,0,0,1,1,1,2], [0,1,0,-1,2,1,1,0,-1,0], [-2,-1,-1,-1,0,0,1,1,1,2], [0,-1,0,1,-2,-1,-1,0,1,0]]

p = [0.02, 0.1, 0.07,0.01, 0.05, 0, 0.1,0.07, 0.01, 0.02]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

board = [list(map(int, input().split(' '))) for _ in range(N)]

x, y = N // 2, N // 2

i = 0
j = 1
k = 0
d = 0

ans = 0

while not (x == 0 and y == 0):
  i += 1

  x += dx[d]
  y += dy[d]

  sand = board[y][x]
  tmp_x, tmp_y = 0,0

  for t in range(10):
    nx,ny = x + t_dx[d][t], y + t_dy[d][t]
    if 0 <= nx < N and 0 <= ny < N: board[ny][nx] += int(board[y][x] * p[t])
    else: ans += int(board[y][x] * p[t])
    sand -= int(board[y][x] * p[t])
    if t == 5: tmp_x, tmp_y = nx, ny

  if 0 <= tmp_x < N and 0 <= tmp_y < N: board[tmp_y][tmp_x] += sand
  else: ans += sand
  board[y][x] = 0

  if i == j and k == 0:
    i = 0
    k += 1
    d = (d + 1) % 4
  if i == j and k == 1:
    i = 0
    j += 1
    k = 0
    d = (d + 1) % 4

print(ans)
