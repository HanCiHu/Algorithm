from copy import deepcopy
from collections import deque

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

N,M,K = map(int, input().split(' '))

board = [[deque([]) for _ in range(N)] for _ in range(N)]
fireball = deque([])

for _ in range(M):
  r,c,m,s,d = map(int,input().split(' '))
  fireball.append((c - 1,r - 1,m,s,d))
  board[r - 1][c - 1].append((c-1,r-1,m,s,d))

for _ in range(K):
  for x,y,m,s,d in fireball:
    nx,ny = (x + dx[d] * s) % N, (y + dy[d] * s) % N
    board[y][x].popleft()
    board[ny][nx].append((nx,ny,m,s,d))
  fireball = []
  for i in range(N):
    for j in range(N):
      if len(board[i][j]) >= 2:
        m = sum(list(map(lambda x: x[2], board[i][j]))) // 5
        s = sum(list(map(lambda x: x[3], board[i][j]))) // len(board[i][j])
        flag = all(list(map(lambda x: x[4] % 2 == 1, board[i][j]))) or all(list(map(lambda x: x[4] % 2 == 0, board[i][j])))
        board[i][j] = deque([])
        if m == 0: continue
        if flag:
          for d in [0,2,4,6]: board[i][j].append((j,i,m,s,d))
        else:
          for d in [1,3,5,7]: board[i][j].append((j,i,m,s,d))
  for i in range(N):
    for j in range(N):
      if len(board[i][j]) > 0:
        for k in board[i][j]:
          fireball.append(deepcopy(k))

cnt = 0

for i in range(N):
  for j in range(N):
    if len(board[i][j]) > 0:
      cnt += sum(list(map(lambda x: x[2], board[i][j])))

print(cnt)