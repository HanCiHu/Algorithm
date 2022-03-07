INF = float('INF')
N = int(input())
M = int(input())

distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
	start, end, weight = map(int, input().split(' '))
	if distance[start][end] > weight:
		distance[start][end] = weight	
	
for k in range(1, N+1): #거치는 점
	for i in range(1, N+1): #시작
		for j in range(1, N+1): #끝
			if i != j and distance[i][j] > distance[i][k] + distance[k][j]:
				distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, len(distance)):
	for j in range(1, len(distance[i])):
		print(0, end=' ') if distance[i][j] == INF else print(distance[i][j], end=' ')
	print()