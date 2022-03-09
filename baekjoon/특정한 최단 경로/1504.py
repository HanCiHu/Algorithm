import sys

input = sys.stdin.readline

N,M = map(int, input().split(' '))
INF = float('INF')

distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
	start, end, weight = map(int, input().split(' '))
	distance[start][end] = weight
	distance[end][start] = weight

v1, v2 = map(int, input().split(' '))

for k in range(1, N + 1):
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			if i == j:
				distance[i][j] = 0
			elif distance[i][j] > distance[i][k] + distance[k][j]:
				distance[i][j] = distance[i][k] + distance[k][j]

ans = min(distance[1][v1] + distance[v1][v2] + distance[v2][N], distance[1][v2] + distance[v2][v1] + distance[v1][N])

print(ans) if distance[1][v1] != INF or distance[v1][v2] != INF or distance[v2][N] != INF or distance[v1][N] != INF else print(-1)