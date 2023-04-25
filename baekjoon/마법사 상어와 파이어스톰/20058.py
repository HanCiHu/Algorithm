from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, Q = map(int ,input().split(' '))
board = [list(map(int ,input().split(' '))) for _ in range(2 ** N)]
steps = list(map(int ,input().split(' ')))

def rotate(proportion):
  new_proportion = list(zip(*reversed(proportion)))
  return new_proportion

def func(s_l, n_l, x,y):
  if n_l < s_l:
    func(s_l // 2, n_l, x,y)
    func(s_l // 2, n_l, x + s_l // 2, y)
    func(s_l // 2, n_l, x, y + s_l // 2)
    func(s_l // 2, n_l, x + s_l // 2, y + s_l // 2)
  if n_l ==s_l:
    new_board = rotate([i[x:x + n_l] for i in board[y:y + n_l]])
    for i in range(s_l):
      for j in range(s_l):
        board[i + y][j + x] = new_board[i][j]

for L in steps:
  func(2 ** N, 2 ** L, 0,0)
  melt = []
  for i in range(2 ** N):
    for j in range(2 ** N):
      cnt = 0
      for k in range(4):
        nx,ny = j + dx[k], i + dy[k]
        if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and board[ny][nx] > 0: cnt += 1
      if cnt < 3: melt.append((j,i))
  for j,i in melt:
    board[i][j] = board[i][j] - 1 if board[i][j] > 0 else 0

cnt = 0
ans = 0

for i in range(2**N):
  for j in range(2**N):
    cnt += board[i][j]
    if board[i][j] > 0:
      q = deque([(j,i)])

      visit = [[False for _ in range(2 ** N)] for _ in range(2 ** N)]
      visit[i][j] = True
      space = 0

      while q:
        x,y = q.popleft()
        space += 1

        for k in range(4):
          nx,ny = x + dx[k], y + dy[k]
          if 0<= nx < 2 ** N and 0 <= ny < 2 ** N and not visit[ny][nx]and board[ny][nx] > 0:
            q.append((nx,ny))
            visit[ny][nx] = True
        ans = max(ans, space)

print(cnt)
if cnt == 0: ans = 0
print(ans)
