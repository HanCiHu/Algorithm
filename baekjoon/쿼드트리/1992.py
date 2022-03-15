n = int(input())
img = [list(map(int, input())) for _ in range(n)]

def check(x, y , l):
  flag = img[y][x]
  for i in range(y, y + l, 1):
    for j in range(x, x + l, 1):
      if img[i][j] != flag:
        return -1
  return flag

def func(x, y, l):
  if (l < 1):
    return
  flag = check(x,y,l)
  if flag != -1:
    print(flag, end='')
  else:
    print('(', end='')
    func(x, y, int(l/2))
    func(x + int(l/2), y, int(l/2))
    func(x, y + int(l/2), int(l/2))
    func(x + int(l/2), y+int(l/2), int(l/2))
    print(')', end='')

func(0,0,n)
