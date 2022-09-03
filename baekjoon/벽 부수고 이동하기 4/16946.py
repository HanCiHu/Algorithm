from collections import deque

N, M = map(int, input().split(' '))

board = [list(map(int, input())) for _ in range(N)]
answer = [[0 for _ in range(M)] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
group = {}

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i, j, group_num):
  q = deque()
  q.append((i,j))
  visit[i][j] = group_num

  ans = 1

  while q:
    y, x = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and ny >= 0 and nx < M and ny < N:
        if board[ny][nx] == 0 and visit[ny][nx] == 0:
          visit[ny][nx] = group_num
          q.append((ny, nx))
          ans += 1
  return ans

def count(y,x):
  cntSet = {}
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and ny >= 0 and nx < M and ny < N:
      if visit[ny][nx] > 0:
        cntSet[visit[ny][nx]] = group[visit[ny][nx]]

  return (sum(cntSet.values()) + 1) % 10

group_num = 1

for i in range(N):
  for j in range(M):
    if (board[i][j] == 0 and visit[i][j] == 0):
      group[group_num] = bfs(i,j, group_num)
      group_num += 1

for i in range(N):
  for j in range(M):
    if (board[i][j] == 0):
      print(0, end='')
    else:
      print(count(i,j), end='')
  print()
