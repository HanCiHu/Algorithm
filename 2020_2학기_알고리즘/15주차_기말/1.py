import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

size = list(map(int, sys.stdin.readline().split(' ')))
money = list(map(int, sys.stdin.readline().split(' ')))
count = list(map(int, sys.stdin.readline().split(' ')))

dp1 = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp = [dp1 for _ in range(10000)]

def func(i, s, value):
	if i >= m:
		return 0
	if dp[i][s][value] > 0:
		return dp[i][s][value]
	a = func(i+1,s,value)
	b = 0
	if count[i] > 0 and s + size[i] <= n:
		count[i] -= 1
		b = money[i] + func(i, s+size[i], value + money[i])
	if a > b :
		dp[i][s][value] = a
	else:
		dp[i][s][value] = b
	return dp[i][s][value]
print(dp[4][10][9999])
print(func(0,0,0))
