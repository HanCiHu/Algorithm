n,m = map(int, input().split(' '))
arr = []
for i in range(n):
	arr.append(list(map(int, input().strip().split(' '))))
dp = [[0 for i in range(m)] for i in range(n)]

for i in range(n - 1,-1,-1):
	for j in range(m):
		if i == n-1:
			dp[i][j] = arr[i][j]
		else:
			if j == 0:
				dp[i][j] = arr[i][j] + max(dp[i+1][j], dp[i+1][j+1])
			elif j == m-1:
				dp[i][j] = arr[i][j] + max(dp[i+1][j], dp[i+1][j-1])
			else:
				dp[i][j] = arr[i][j] + max(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1])

a = 0
for i in range(m):
	if dp[0][i] > a:
		a = dp[0][i]
print(a)