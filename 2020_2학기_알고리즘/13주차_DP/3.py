n = int(input())
m = list(map(int, input().split(' ')))
target = int(input())

dp = [0 for i in range(target + 1)]

for i in range(1, target+1, 1):
	lst = []
	for j in m:
		if i - j >= 0:
			lst.append(j)
	temp = 100000
	for j in lst:
		temp = min(temp, int(dp[i-j]) + 1)
	dp[i] = temp

print(dp[target])
