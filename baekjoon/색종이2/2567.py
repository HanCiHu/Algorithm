N = int(input())
paper = [tuple(map(int, input().split(' '))) for _ in range(N)]

c = [[0 for _ in range(101)] for _ in range(101)]

for x,y in paper:
  for i in range(x, x + 10 ,1):
    for j in range(y, y + 10, 1):
      c[j][i] += 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0

for i in range(101):
  for j in range(101):
    if c[i][j] > 0:
      for k in range(4):
        if c[i + dx[k]][j + dy[k]] == 0: ans += 1

print(ans)