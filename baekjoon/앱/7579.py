INF = float('inf')

N, M =map(int, input().split(' '))

mem = list(map(int, input().split(' ')))
cost = list(map(int, input().split(' ')))

size = sum(cost)
ans = size

dp = [[0 for _ in range(size + 1)] for _ in range(N)]

for i in range(N):
	m = mem[i]
	c = cost[i]

	for j in range(1, size + 1, 1):
		if j < c:
			dp[i][j] = dp[i - 1][j]

