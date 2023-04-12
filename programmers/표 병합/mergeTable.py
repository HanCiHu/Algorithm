def solution(commands):
  board = [[[(i * 50) + j + 1, ''] for j in range(50)] for i in range(50)]
  answer = []
  cnt = 2501
  for cmd in commands:
    parse = cmd.split(' ')
    if parse[0] == 'UPDATE' and len(parse) == 4: # r,c, value
      r,c = int(parse[1]) - 1, int(parse[2]) - 1
      uid = board[r][c][0]
      for y in range(50):
        for x in range(50):
          if board[y][x][0] == uid:
            board[y][x][1] = parse[3]

    elif parse[0] == 'UPDATE' and len(parse) == 3: # value1 to value2
      for i in range(50):
        for j in range(50):
          if board[i][j][1] == parse[1]:
            board[i][j][1] = parse[2]
    elif parse[0] == 'MERGE': # r1, c1, r2,c2
      r1,c1,r2,c2 = int(parse[1]) - 1, int(parse[2]) - 1,int(parse[3]) - 1,int(parse[4]) - 1
      uid1 = board[r1][c1][0]
      value1 = board[r1][c1][1]
      uid2 = board[r2][c2][0]
      value2 = board[r2][c2][1]
      value = value2 if value1 == '' else value1
      for y in range(50):
        for x in range(50):
          if board[y][x][0] == uid1 or board[y][x][0] == uid2:
            board[y][x][1] = value
            board[y][x][0] = cnt
      cnt += 1

    elif parse[0] == 'UNMERGE': #r c
      r,c = int(parse[1]) - 1, int(parse[2]) - 1
      [uid, value] = board[r][c]
      for y in range(50):
        for x in range(50):
          if board[y][x][0] == uid:
            board[y][x][0] = cnt
            board[y][x][1] = ''
            cnt += 1
      board[r][c][1] = value
    elif parse[0] == 'PRINT': # print r c
      r,c = int(parse[1]) - 1, int(parse[2]) - 1
      if board[r][c][1] == '':
        answer.append("EMPTY")
      else:
        answer.append(board[r][c][1])
  return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))