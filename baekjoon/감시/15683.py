from copy import deepcopy
N, M = map(int, input().split(' '))
board = [list(map(int, input().split(' '))) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cctv_type = [[], [[0],[1],[2],[3]], [[0,1], [2,3]], [[0,3], [0,2], [1,2],[1,3]], [[0,1,2], [0,1,3],[0,2,3],[1,2,3]], [[0,1,2,3]]]

cctvs = []

for i in range(N):
  for j in range(M):
    if 1 <= board[i][j] <= 5:
      cctvs.append((j,i))

ans = 99999999

def check(board, x, y, d):
  while x >= 0 and x < M and y >= 0 and y < N:
    if board[y][x] == 0: board[y][x] = -1
    elif board[y][x] == 6: break
    x += dx[d]
    y += dy[d]

def func(board, dep):
  global ans
  if dep == len(cctvs):
    cnt = 0
    for i in range(N):
      for j in range(M):
        if board[i][j] == 0: cnt += 1
    ans = min(ans, cnt)
    return 

  board_tmp = deepcopy(board)
  x,y = cctvs[dep]
  t = board[y][x]
  for i in range(len(cctv_type[t])):
    for j in range(len(cctv_type[t][i])):
      check(board_tmp, x, y, cctv_type[t][i][j])
    func(board_tmp, dep + 1)
    board_tmp = deepcopy(board)

func(board, 0)

print(ans)

