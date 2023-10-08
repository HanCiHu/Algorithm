N = int(input())
arr = [input() for _ in range(N)]
rank = [[0, i] for i in range(N)] # win_count, index

for i in range(N):
  for j in range(N):
    if i == j: continue
    if arr[i][j] == 'o': rank[i][0] = rank[i][0] + 1
    else: rank[j][0] = rank[j][0] + 1

rank.sort(key= lambda x: (x[0], -x[1]), reverse=True)

for i in rank: print(i[1] + 1, end=" ")
