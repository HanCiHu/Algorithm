def solution(rows, columns, queries):
  board = [[j * columns + i + 1  for i in range(columns)] for j in range(rows)]
  ans = []
  for q in queries:
    q = map(lambda x: x - 1, q)
    m = 100001
    [y1,x1,y2,x2] = q
    tmp = board[y1][x1]
    for i in range(x1, x2):
      m = min(tmp, m)
      tmp1 = board[y1][i + 1]
      board[y1][i + 1] = tmp
      tmp = tmp1
    for i in range(y1, y2):
      m = min(tmp, m)
      tmp1 = board[i + 1][x2]
      board[i + 1][x2] = tmp
      tmp = tmp1
    for i in range(x2, x1, -1):
      m = min(tmp, m)
      tmp1 = board[y2][i - 1]
      board[y2][i - 1] = tmp
      tmp = tmp1
    for i in range(y2, y1, -1):
      m = min(tmp, m)
      tmp1 = board[i - 1][x1]
      board[i - 1][x1] = tmp
      tmp = tmp1
    ans.append(m)
  return ans

print(solution(6, 7, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))