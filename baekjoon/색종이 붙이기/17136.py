board = [list(map(int, input().split(' '))) for _ in range(10)]

cnt = [0,0,0,0,0,0]

def patch(x, y, board, length):
  for i in range(length):
    for j in range(length):
      board[y + i][x + j] = 0

def detach(x,y,board, length):
  for i in range(length):
    for j in range(length):
      board[y+i][x+j] = 1

def can_patch(x,y,board,length):
  for i in range(length):
    for j in range(length):
      if board[y + i][x + j] == 0: return False
  return True

def check(board):
  for i in range(10):
    for j in range(10):
      if board[j][i] == 1: return False
  return True

ans = float('inf')

def func(board, x, y, c):
  global ans
  if check(board):
    ans = min(c,ans)
    return
  if x == 10: return func(board, 0, y + 1, c)
  if y == 10:
    ans = min(c, ans)
    return
  
  if board[y][x] == 1:
    for l in range(1, 6, 1):
      if cnt[l] >= 5: continue
      if x + l > 10 or y + l > 10: continue
      if not can_patch(x,y,board,l): break
      patch(x, y, board, l)
      cnt[l] += 1
      func(board, x + 1, y, c + 1)
      cnt[l] -= 1
      detach(x,y,board, l)
  else:
    func(board, x + 1, y, c)

func(board, 0,0, 0)
print(ans if ans != float('inf') else -1)