def check(board, flag):
  x_board = list(map(lambda x: x == flag, board))

  x_flag = all([j for i,j in enumerate(x_board) if i < 3])
  x_flag = x_flag or all([j for i,j in enumerate(x_board) if 3 <= i < 6])
  x_flag = x_flag or all([j for i,j in enumerate(x_board) if 6 <= i < 9])
  x_flag = x_flag or all([j for i,j in enumerate(x_board) if i % 3 == 0])
  x_flag = x_flag or all([j for i,j in enumerate(x_board) if i % 3 == 1])
  x_flag = x_flag or all([j for i,j in enumerate(x_board) if i % 3 == 2])
  x_flag = x_flag or x_board[0] == x_board[4] == x_board[8] == True
  x_flag = x_flag or x_board[2] == x_board[4] == x_board[6] == True

  return x_flag

while True:
  game = input().rstrip()
  if game == 'end': break
  if game.count('O') != game.count('X') and game.count('O') + 1 != game.count('X') :
    print('invalid')
    continue
  if not (check(game, 'X') or check(game, 'O')) and len(list(filter(lambda x: x == '.', game))) > 0:
    print('invalid')
    continue
  if check(game, 'O') and game.count('O') != game.count('X'):
    print('invalid')
    continue
  if check(game, 'X') and game.count('O') + 1 != game.count('X'):
    print('invalid')
    continue
  print('valid')
