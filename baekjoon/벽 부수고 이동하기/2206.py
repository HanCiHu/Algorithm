from collections import deque
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def countDis(maps):
  visit = [[0 for _ in range(M)] for _ in range(N)]
  q = deque([(0,0)])

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < M and ny >= 0 and ny < N:
        if maps[ny][nx] == '0' and visit[ny][nx] == 0:
          q.append((nx,ny))
          visit[ny][nx] = visit[y][x] + 1
  return visit[N - 1][M - 1] + 1

def breakWall():
  ans = -1
  for n in range(N):
    for m in range(M):
      if maps[n][m] == '1':
        newMaps = copy.deepcopy(maps)
        newMaps[n][m] = '0'
        dis = countDis(newMaps)
        if dis > 1 and dis > ans:
          ans = dis
  return ans


N, M = map(int , input().split(' '))
maps = [list(input()) for _ in range(N)]

print(breakWall())
