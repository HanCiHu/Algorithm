N, M = map(int, input().split(' '))

board = [input() for _ in range(N)]

leftTop = ["###.", "###.", "###.","...."]
rightBottom = ["....", ".###", ".###",".###"]

def check(arr):
  if [row[:4] for row in arr[:4]] != leftTop: return False
  if [row[5:9] for row in arr[5:9]] != rightBottom: return False
  return True

for i in range(N - 8):
  for j in range(M - 8):
    if board[i][j] == '#':
      if check([row[j:j+9] for row in board[i:i+9]]):
        print(i + 1,j + 1)
