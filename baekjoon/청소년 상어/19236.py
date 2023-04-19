from copy import deepcopy

dx = [0,0, -1,-1,-1,0,1,1,1]
dy = [0,-1, -1,0,1,1,1,0,-1]

board = [[0 for _ in range(4)] for _ in range(4)] # 물고기 정보 저장
fish = {} # 좌표, 방향 저장

for i in range(4):
  f_info = list(map(int, input().split(' ')))
  for j in range(0,8,2):
    fish[f_info[j]] = (j//2, i, f_info[j + 1])
    board[i][j//2] = f_info[j]

ans = board[0][0]
shark = (0,0,fish[board[0][0]][2]) # 좌표, 방향
fish[board[0][0]] = (-1,-1,-1) # 잡아먹힘
board[0][0] = 0 # 0이면 상어, -1이면 빈 공간

def func(shark, board, fish, cnt):
  global ans
  if shark[0] < 0 or shark[0] >= 4 or shark[1] < 0 or shark[1] >= 4:
    ans = max(ans, cnt)
    return
  for i in range(1, 17, 1):
    x,y,d = fish[i]
    if x == -1 or y == -1: continue
    while True:
      nx, ny = x + dx[d], y + dy[d]
      if nx >= 0 and ny >= 0 and nx < 4 and ny < 4 and board[ny][nx] != 0: break
      d = d + 1
      if d == 9: d = 1
    fish[i] = (nx,ny,d)
    if board[ny][nx] > 0: fish[board[ny][nx]] = (x,y,fish[board[ny][nx]][2])
    board[y][x] = board[ny][nx]
    board[ny][nx] = i

  i = 1
  while True:
    tmp_shark = deepcopy(shark)
    x,y,d = tmp_shark
    nx = x + (dx[d] * i)
    ny = y + (dy[d] * i)
    if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
      func((-1,-1,-1), board, fish, cnt)
      break
    tmp_board = deepcopy(board)
    tmp_fish = deepcopy(fish)
    if board[ny][nx] == -1:
      i+=1
      continue
    else: tmp_shark = (nx, ny, tmp_fish[tmp_board[ny][nx]][2])

    tmp = tmp_board[ny][nx] # 원래 자리에 있던 물고기 크기
    tmp_fish[tmp] = (-1,-1,-1) # 잡아 먹힘
    tmp_board[ny][nx] = 0 # 상어자리
    tmp_board[y][x] = -1 # 빈자리 (이전 상어 자리)
    func(tmp_shark, tmp_board, tmp_fish, cnt + tmp)
    i+=1

func(shark, board, fish, ans)

print(ans)