N = int(input())
INF = float('inf')

house = []

for i in range(N):
	r,g,b = map(int, input().split(' '))
	house.append([r,g,b])

ans = INF

for i in range(3):
	dp = [[INF, INF, INF] for _ in range(N)]
	dp[0][i] = house[0][i]

	for j in range(1, N, 1):
		dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + house[j][0]
		dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + house[j][1]
		dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + house[j][2]
	
	for j in range(3):
		if i != j:
			ans = min(ans, dp[-1][j])

print(ans)