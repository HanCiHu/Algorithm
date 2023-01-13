from collections import deque
from itertools import permutations

w,h = map(int, input().split(' '))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def calDist(start, end):
	q = deque([(start[0], start[1], 0)])
	visit = [[False for _ in range(w)] for _ in range(h)]

	while q:
		x, y, cnt = q.popleft()
		if x == end[0] and y == end[1]:
			return cnt

		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if nx >= 0 and ny >= 0 and nx < w and ny < h and not visit[ny][nx] and arr[ny][nx] != 'x':
				q.append((nx, ny, cnt + 1))
				visit[ny][nx] = True

while w != 0 or h != 0:
	arr = [list(input()) for _ in range(h)]
	visit = [[False for _ in range(w)] for _ in range(h)]
	dusts = []
	robot = (0,0)

	for i in range(w):
		for j in range(h):
			if arr[j][i] == 'o': robot = (i,j)
			elif arr[j][i] == '*': dusts.append((i,j))

	distance = [[-1 for _ in range(len(dusts))] for _ in range(len(dusts))]

	for i in range(0, len(dusts), 1):
		for j in range(0, len(dusts), 1):
			if i == j: distance[i][j] = 0
			distance[i][j] = calDist(dusts[i], dusts[j])

	robot_dist = [-1 for _ in range(len(dusts))]

	q = deque([(robot[0], robot[1], 0)])
	visit = [[False for _ in range(w)] for _ in range(h)]

	while q:
		x,y, cnt = q.popleft()
		if arr[y][x] == '*':
			robot_dist[dusts.index((x,y))] = cnt

		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if nx >= 0 and ny >= 0 and nx < w and ny < h and not visit[ny][nx] and arr[ny][nx] != 'x':
				visit[ny][nx] = True
				q.append((nx,ny,cnt + 1))
	
	perm = permutations([i for i in range(len(dusts))], len(dusts))

	ans = 9999999999

	if -1 in robot_dist: print(-1)
	else:
		for p in perm:
			tmp = robot_dist[p[0]]
			for i in range(1, len(p), 1):
				tmp += distance[p[i - 1]][p[i]]
			ans = min(ans, tmp)
		print(ans)
	
	w,h = map(int, input().split(' '))
