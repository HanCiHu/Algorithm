from collections import defaultdict

dx = [0,0,0,-1,1]
dy = [0,-1,1,0,0]

cx = [-1,0,1,0]
cy = [0,1,0,-1]

"""
1. 구슬을 파괴하는 단계
2. 파괴된 구슬을 채우는 단계
3. 연속하는 구슬을 파괴하는 단계
4. 파괴된 구슬을 채우는 단계
5. 3~4번 반복 (연속하는 구슬이 없을 때 까지)
6. 그룹화 한 구슬을 두개로 나누는 과정 (구슬의 개수, 구슬의 번호)
"""

N,M = map(int, input().split(' '))

board = [list(map(int ,input().split(' '))) for _ in range(N)]

ans = defaultdict(int)

def init_board(l):
  if len(l) == 0: return []
  standard = l[0]
  cnt = 1
  arr = []
  for i in range(1, len(l)):
    if l[i] == standard: cnt += 1
    else:
      arr.append((standard, cnt))
      cnt = 1
      standard = l[i]
  arr.append((standard, cnt))
  return arr

def delete_board(l):
  arr = []
  for s,c in l:
    if c >= 4: ans[s] += c
    else: arr.append((s,c))
  return arr

def union(l):
  if len(l) == 0: return []
  s, c = l[0]
  arr = []
  for i in range(1, len(l)):
    if l[i][0] == s: c += l[i][1]
    else:
      arr.append((s,c))
      s,c = l[i]
  arr.append((s,c))
  return arr


def check(l):
  for s,c in l:
    if c >= 4: return False
  return True

def set_board(l):
  x, y = N // 2 - 1, N // 2
  arr_i = 0
  i = 0
  j = 1
  k = 1
  d = 1

  arr = []

  for s,c in l:
    arr.append(c)
    arr.append(s)

  while 0 <= x < N and 0 <= y < N:
    if arr_i >= len(arr): board[y][x] = 0
    else: board[y][x] = arr[arr_i]
    x,y = x + cx[d], y + cy[d]
    i += 1
    arr_i += 1

    if i == j and k % 2 == 1:
      i = 0
      j += 1
      k += 1
      d = (d + 1) % 4

    elif i == j and k % 2 == 0:
      i = 0
      k += 1
      d = (d + 1) % 4

def make_linear():
  x, y = N // 2 - 1, N // 2

  i = 0
  j = 1
  k = 1
  d = 1

  linear_board = []

  while 0 <= x < N and 0 <= y < N and board[y][x] != 0:
    if board[y][x] > 0: linear_board.append(board[y][x])
    x,y = x + cx[d], y + cy[d]
    i += 1

    if i == j and k % 2 == 1:
      i = 0
      j += 1
      k += 1
      d = (d + 1) % 4

    elif i == j and k % 2 == 0:
      i = 0
      k += 1
      d = (d + 1) % 4
  return linear_board

def blzard():
  linear_board = make_linear()
  linear_board = init_board(linear_board)

  while True:
    linear_board = delete_board(linear_board)
    linear_board = union(linear_board)
    if check(linear_board): break
  
  set_board(linear_board)

for _ in range(M):
  d,s = map(int, input().split(' '))
  x, y = N // 2, N // 2
  for i in range(1, s + 1, 1):
    nx,ny = x + dx[d] * i, y + dy[d] * i
    board[ny][nx] = -1
  blzard()

answer = 0
for i in ans: answer += ans[i] * i

print(answer)