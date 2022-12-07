from collections import deque

board = [[int(i) for i in map(str, input())] for _ in range(9)]

empty = deque()

for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      empty.append((j,i))

def checkColumn(n, y):
  for i in range(9):
    if board[y][i] == n:
      return False
  return True

def checkRow(n, x):
  for i in range(9):
    if board[i][x] == n:
      return False
  return True

def checkBox(x,y, n):
  sx = (x // 3) * 3
  sy = (y // 3) * 3

  for i in range(sx, sx + 3, 1):
    for j in range(sy, sy + 3, 1):
      if board[j][i] == n:
        return False
  return True

def fillBoard(n):
  if n == len(empty):
    for i in board:
      print(''.join([j for j in map(str, i)]))
    exit()

  (x, y) = empty[n]

  for i in range(1, 10, 1):
    if checkColumn(i, y) and checkRow(i, x) and checkBox(x, y, i):
      board[y][x] = i
      fillBoard(n + 1)
      board[y][x] = 0

fillBoard(0)
