dx = [0, 0,0,-1,1]
dy = [0, -1,1,0,0]

N, M, k = map(int, input().split(' '))

board = [list(map(int, input().split(' '))) for _ in range(N)] # 상어 종류, 냄새 종류, 남은 냄새
first_direction = [0] + list(map(int,input().split(' '))) #초기 상어 방향

for i in range(N):
  board[i] = list(map(lambda x: [x, x, k] if x > 0 else [0,0,0], board[i]))
shark_info = {} # 상어들 좌표, 방향 (x,y,d)

for i in range(N):
  for j in range(N):
    if board[i][j][0] > 0:
      shark_info[board[i][j][0]] = [j,i, first_direction[board[i][j][0]]]

shark_like = {} # 상어들의 선호도
for i in range(1, M + 1, 1):
  shark_like[i] = [0] + [list(map(int, input().split(' '))) for _ in range(4)]

def check_shark():
  cnt = 0
  for i in range(1, M + 1, 1):
    if shark_info[i][0] != -1: cnt += 1
    if cnt >= 2: return True
  return False

def decrease_smell():
  for i in range(N):
    for j in range(N):
      if board[i][j][2] > 0:
        board[i][j][2] -= 1

def delete_shark():
  for i in range(1, M + 1, 1):
    if shark_info[i][0] == -1: continue
    for j in range(i + 1, M + 1, 1):
      if shark_info[j][0] == -1: continue
      if shark_info[i][0] == shark_info[j][0] and shark_info[i][1] == shark_info[j][1]:
        x,y,d = shark_info[j]
        board[y][x] = [i,i,k]
        shark_info[j] = (-1,-1,-1)

cnt = 0

while check_shark():
  if cnt >= 1000:
    print(-1)
    exit()
  shark_moved = []
  for i in range(1, M + 1, 1):
    x,y,d = shark_info[i]
    if x == -1 and y == -1: continue
    is_moved = False
    for j in range(4): # 빈 칸 이동
      nx, ny = x + dx[shark_like[i][d][j]], y + dy[shark_like[i][d][j]]
      if nx >= 0 and ny >= 0 and nx < N and ny < N and board[ny][nx][2] < 1:
        shark_moved.append((i, x, y, nx, ny, shark_like[i][d][j]))
        shark_info[i] = (nx,ny,shark_like[i][d][j])
        is_moved = True
        break

    if is_moved: continue

    for j in range(4): # 냄새 칸 이동
        nx, ny = x + dx[shark_like[i][d][j]], y + dy[shark_like[i][d][j]]
        if nx >= 0 and ny >= 0 and nx < N and ny < N and board[ny][nx][1] == i:
          shark_moved.append((i, x, y, nx, ny, shark_like[i][d][j]))
          shark_info[i] = (nx,ny,shark_like[i][d][j])
          break

  decrease_smell()
  delete_shark()

  for m in shark_moved:
    i,x,y,nx,ny,d = m
    if shark_info[i][0] == -1 and shark_info[i][1] == -1: continue
    board[ny][nx] = [i,i,k]
    board[y][x][0] = 0

  cnt += 1

print(cnt)

