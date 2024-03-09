from copy import deepcopy

N = int(input())
board = [list(map(int, input().split(' '))) for _ in range(N)]

ans = max(list(map(lambda x: max(x), board)))

def move(t, board):
  temp_board = [[0 for _ in range(N)] for _ in range(N)]
  if t == 0: # 위로 올리기
    for i in range(N):
      temp = -1
      board_line = []
      for j in range(N):
        if board[j][i] == 0: continue
        if temp == board[j][i]:
          board_line.pop()
          board_line.append(board[j][i] * 2)
          temp = -1
        else:
          board_line.append(board[j][i])
          temp = board[j][i]
      
      board_line += [0 for _ in range(N)]
      board_line = board_line[:N]

      for j in range(N): temp_board[j][i] = board_line[j]

  elif t == 1: # 오른쪽으로 밀기
    for i in range(N):
      temp = -1
      board_line = []
      for j in range(N - 1, -1, -1):
        if board[i][j] == 0: continue
        if temp == board[i][j]:
          board_line.pop()
          board_line.append(board[i][j] * 2)
          temp = -1
        else:
          board_line.append(board[i][j])
          temp = board[i][j]

      board_line += [0 for _ in range(N)]
      board_line = board_line[:N]

      for j in range(N): temp_board[i][j] = board_line[N - j - 1]

  elif t == 2: # 아래로 내리기
    for i in range(N):
      temp = -1
      board_line = []
      for j in range(N - 1, -1, -1):
        if board[j][i] == 0: continue
        if temp == board[j][i]:
          board_line.pop()
          board_line.append(board[j][i] * 2)
          temp = -1
        else:
          board_line.append(board[j][i])
          temp = board[j][i]

      board_line += [0 for _ in range(N)]
      board_line = board_line[:N]

      for j in range(N): temp_board[N - j - 1][i] = board_line[j]

  elif t == 3: # 왼쪽으로 밀기
    for i in range(N):
      temp = -1
      board_line = []
      for j in range(N):
        if board[i][j] == 0: continue
        if temp == board[i][j]:
          board_line.pop()
          board_line.append(board[i][j] * 2)
          temp = -1
        else:
          board_line.append(board[i][j])
          temp = board[i][j]

      board_line += [0 for _ in range(N)]
      board_line = board_line[:N]

      for j in range(N): temp_board[i][j] = board_line[j]
  return temp_board

def func(i, board):
  global ans
  if i == 5:
    ans = max(list(map(lambda x: max(x), board)) + [ans])
    return
  for j in range(4):
    new_board = move(j, board)
    func(i + 1, new_board)

func(0, board)

print(ans)