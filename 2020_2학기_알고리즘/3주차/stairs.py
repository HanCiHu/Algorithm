def stairs(n):
	if n <= 1:
		return 1
	elif n == 2:
		return stairs(0) + stairs(1)
	else:
		return stairs(n - 1) + stairs(n - 2)

def dy_stairs(n):
	dp = [int(0) for _ in range(n + 1)]
	dp[0] = 1
	dp[1] = 1
	for i in range(2, n+1, 1):
		dp[i] = dp[i - 1] + dp[i - 2]
	return dp[n]


print(dy_stairs(4))
