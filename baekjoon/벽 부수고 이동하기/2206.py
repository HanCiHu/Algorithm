from collections import deque
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
  visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
  q = deque([(0,0,0)])

  while q:
    x, y, isCrashed = q.popleft()

    if x == M - 1 and y == N - 1:
      return visit[y][x][isCrashed] + 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < M and ny >= 0 and ny < N:
        if maps[ny][nx] == '0' and visit[ny][nx][isCrashed] == 0:
          q.append((nx,ny, isCrashed))
          visit[ny][nx][isCrashed] = visit[y][x][isCrashed] + 1
        if maps[ny][nx] == '1' and isCrashed == 0:
          q.append((nx, ny, isCrashed + 1))
          visit[ny][nx][isCrashed + 1] = visit[y][x][isCrashed] + 1
  return -1


N, M = map(int , input().split(' '))
maps = [list(input()) for _ in range(N)]

print(bfs())
