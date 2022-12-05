from collections import deque

N, M = map(int, input().split(' '))
board = [[i for i in map(int, input())] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0

for i in range(N):
  for j in range(M):
    if board[i][j] == 1:
      continue
    q = deque()
    q.append((i,j))
    board[i][j] = 1
    while q:
      y,x = q.popleft()

      for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y

        if nx >= 0 and ny >= 0 and nx < M and ny < N and board[ny][nx] == 0:
          board[ny][nx] = 1
          q.append((ny, nx))
    cnt += 1

print(cnt)