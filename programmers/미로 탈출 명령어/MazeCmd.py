import sys;sys.setrecursionlimit(10000)

cmd = ['d', 'l', 'r', 'u']
dx = [1,0,0,-1]
dy = [0,-1,1,0]

g_ans = ''
dp = [[['' for _ in range(2501)] for _ in range(51)] for _ in range(51)]

def func(n,m,x,y,r,c,k,ans):
  global g_ans
  if g_ans != '': return
  if k == 0 and x == r and y == c and g_ans == '':
    g_ans = ans
    return
  if k == 0: return

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]

    if 0 < nx <= n and 0 < ny <= m and abs(nx - r) + abs(ny - c) <= k:
      if dp[nx][ny][k - 1] == '':
        dp[nx][ny][k - 1] = ans + cmd[i]
        func(n,m,nx,ny,r,c,k - 1, ans + cmd[i])
  return

def solution(n,m,x,y,r,c,k):
  z = k - abs(x - r) + abs(y - c)
  if z < 0 or z % 2 != 0:
    return 'impossible'

  func(n,m,x,y,r,c,k,'')

  return g_ans if g_ans != '' else 'impossible'


# print(solution(3, 4, 2, 3, 3, 1, 5))
# print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))
