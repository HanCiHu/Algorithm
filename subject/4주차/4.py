num = int(input())
coin_list = list(map(int, input().split(' ')))
target = int(input())
coin_list.sort()
dp = [99999] * (target+1)
dp[0] = 0
coins = list()
def func(i):
	n = target
	lst = [0] * num
	for j in range(i, -1, -1):
		count = n // coin_list[j]
		n = n - count * coin_list[j]
		lst[j] = count
	return lst
for i in range(num):
	for j in range(coin_list[i], target + 1, 1):
		if dp[j] > dp[j-coin_list[i]]+1 and j == target:
			coins = func(i)
		dp[j] = min(dp[j], dp[j - coin_list[i]] + 1)
for i in range(num):
	if coins[i] != 0:
		print(coin_list[i], coins[i])
