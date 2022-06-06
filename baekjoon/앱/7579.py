INF = float('inf')

N, M =map(int, input().split(' '))

mem = list(map(int, input().split(' ')))
cost = list(map(int, input().split(' ')))

dp = [INF for _ in range(M + 1)]

for i in cost:
	for j in range(M, i + 1, -1):
		if dp[j - i] != INF:
			dp[j] = min(dp[j - i] + i, dp[j])
		else:
			dp[j] = min(i, dp[j])
print(dp[M])