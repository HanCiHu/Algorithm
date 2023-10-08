N,M = map(int, input().split())
points = list(map(int, input().split()))
solved = [input() for _ in range(N)]

users_points = [(sum([points[i] for i in range(M) if solved[j][i] == 'o']) + j + 1) for j in range(N)]
max_point = max(users_points)

points = [(value, index) for index, value in enumerate(points)]
points.sort(reverse=True)

answer = []

for i in range(N):
  cnt = 0
  for value,index in points:
    if max_point == users_points[i]: break
    if solved[i][index] == 'o' : continue

    users_points[i] += value
    cnt += 1

    if max_point < users_points[i]: break
  answer.append(cnt)

for i in answer: print(i)