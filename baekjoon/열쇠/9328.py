from collections import deque
T = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(T):
  h, w = map(int, input().split(' '))
  building = deque([list('.' + input() + '.') for i in range(h)])
  building.appendleft(['.' for _ in range(w + 2)])
  building.append(['.' for _ in range(w + 2)])
  keys = input()
  if keys == '0': keys = ''
  visit = [[False for i in range(w + 2)] for i in range(h + 2)]

  q = deque([(0,0)])

  ans = 0

  while q:
    x,y = q.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if 0 <= nx < w + 2 and 0 <= ny < h + 2 and not visit[ny][nx]:
        if building[ny][nx] == '*': continue

        elif building[ny][nx] == '.':
          visit[ny][nx] = True
          q.append((nx, ny))
        
        elif building[ny][nx].islower():
          visit = [[False for i in range(w + 2)] for i in range(h + 2)]
          q.append((nx,ny))
          visit[ny][nx] = True
          keys += building[ny][nx]
          building[ny][nx] = '.'
        
        elif building[ny][nx].isupper() and building[ny][nx].lower() in keys:
          visit[ny][nx] = True
          q.append((nx, ny))
          building[ny][nx] = '.'
        
        elif building[ny][nx] == '$':
          ans += 1
          building[ny][nx] = '.'
          q.append((nx, ny))
          visit[ny][nx] = True
  print(ans)