import heapq

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())
board = [input() for _ in range(M)]
visit = [[False for _ in range(N)] for _ in range(M)]
q = [(0, 0, 0)]

while q:
  b, x, y = heapq.heappop(q)
  if x == N  - 1 and y == M - 1:
    print(b)
    exit(0)
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and not visit[ny][nx]:
      if board[ny][nx] == '1':
        heapq.heappush(q, (b + 1, nx, ny))
      elif board[ny][nx] == '0':
        heapq.heappush(q, (b, nx, ny))
      visit[ny][nx] = True