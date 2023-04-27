dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

diagonal_x = [-1,-1,1,1]
diagonal_y = [-1,1,-1,1]

N,M = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]
cloud = [(0, N-1), (0,N-2), (1,N-1), (1,N-2)]
cmd = [list(map(int, input().split(' '))) for _ in range(M)]

for c in cmd:
  d,s = c[0], c[1]
  moved_cloud = []
  for x,y in cloud:
    nx,ny = (x + dx[d] * s) % N, (y + dy[d] * s) % N
    moved_cloud.append((nx,ny))
  for x,y in moved_cloud: board[y][x] += 1

  cloud = []
  add_bucket = []
  for x,y in moved_cloud:
    for i in range(4):
      nx, ny = x + diagonal_x[i], y + diagonal_y[i]
      if 0 <= nx < N and 0 <= ny < N and board[ny][nx] > 0:
        add_bucket.append((x, y))

  for  x,y in add_bucket: board[y][x] += 1

  for i in range(N):
    for j in range(N):
      if board[i][j] >= 2 and (j,i) not in moved_cloud:
        board[i][j] -= 2
        cloud.append((j,i))

cnt = 0

for i in board: cnt += sum(i)
print(cnt)