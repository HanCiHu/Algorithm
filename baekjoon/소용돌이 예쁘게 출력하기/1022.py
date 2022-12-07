y1,x1,y2,x2 = map(int, input().split(' '))

board = [[0 for _ in range(x2 - x1 + 1)] for _ in range(y2 - y1 + 1)]
n = 1
x = 0
y = 0

d = 0
cnt = 0
i = 0
flag = 0

f = (x2 - x1 + 1) * (y2 - y1 + 1)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

while flag < f:
  if x1 <= x <= x2 and y1 <= y <= y2:
    board[y - y1][x - x1] = n
    flag += 1
  x += dx[d]
  y += dy[d]
  n += 1
  if i == cnt:
    d += 1
    if d % 4 == 0: d = 0
    if d == 0 or d == 2: cnt += 1
    i = 0
  else:
    i += 1

for i in range(y2-y1+1):
    for j in range(x2-x1+1):
        print(str(board[i][j]).rjust(len(str(n - 1))), end=" ")
    print()