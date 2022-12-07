n = int(input())
n2 = n * n

board = [list(map(int, input().split(' '))) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]

ans = 0

def checkBishop(x,y):
  nx, ny = x,y
  while 0 <= nx < n and 0 <= ny < n:
    if visit[ny][nx]:
      return False
    nx += 1
    ny += 1
  
  nx, ny = x,y
  while 0 <= nx < n and 0 <= ny < n:
    if visit[ny][nx]:
      return False
    nx -= 1
    ny += 1

  nx, ny = x,y
  while 0 <= nx < n and 0 <= ny < n:
    if visit[ny][nx]:
      return False
    nx -= 1
    ny -= 1

  nx, ny = x,y
  while 0 <= nx < n and 0 <= ny < n:
    if visit[ny][nx]:
      return False
    nx += 1
    ny -= 1

  return True

def btk(a, cnt, mode):
  global ans
  for i in range(a, n2, 1):
    x = i % n
    y = i // n

    if (x + y) % 2 == mode:
      continue

    if board[y][x] == 1 and not visit[y][x] and checkBishop(x,y):
      visit[y][x] = True
      ans = max(ans, cnt + 1)
      btk(i + 1, cnt + 1, mode)
      visit[y][x] = False
  return ans


a = btk(0,0, 1)
ans = 0
b = btk(0,0, 0)
print(a+b)