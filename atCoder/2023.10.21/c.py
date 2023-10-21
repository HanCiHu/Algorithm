from collections import deque

N,M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [1,-1,1,-1,1,-1,0,0]
dy = [1,-1,-1,1,0,0,1,-1]

ans = 0

def check_sensor(sx,sy):
  q = deque([(sx,sy)])
  while q:
    x,y = q.popleft()
    for i in range(8):
      nx,ny = x + dx[i], y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == '#':
        board[ny][nx] = '.'
        q.append((nx,ny))

for i in range(N):
  for j in range(M):
    if board[i][j] == '#':
      board[i][j] = '.'
      check_sensor(j,i)
      ans += 1

print(ans)
