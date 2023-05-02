dx = [0,1,0,-1]
dy = [-1,0,1,0]

N = int(input())
M = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

x = N // 2
y = N // 2

i = 1 # 달팽이가 적을 자리
j = 0 # 몇번째 전진 중인가요?
k = 1 # 몇번이나 전진하고 방향을 바꿔야하나요?
l = 0 # 이번에 전진 횟수를 늘려야하나요?
d = 0

while x >= 0 and y >= 0:
  board[y][x] = i
  x, y = x + dx[d], y + dy[d]
  i += 1

  j += 1
  if j == k and l == 0: # 전진 횟수 안바꾸기
    d = (d + 1) % 4
    j = 0
    l += 1
  elif j == k and l == 1: # 전진 횟수 바꾸기
    j = 0
    k += 1
    l = 0
    d = (d + 1) % 4

ansx = 0
ansy = 0

for i in range(N):
  for j in range(N):
    print(board[i][j], end=" ")
    if board[i][j] == M:
      ansx = i + 1
      ansy = j + 1
  print()
print(ansx, ansy)
