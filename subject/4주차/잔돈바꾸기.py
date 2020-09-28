def func(coin_list, target):
	min_coins = target
	if target in coin_list:
		return 1
	else:
		coins = list()
		for i in coin_list:
			if i <= target:
				conis.append(i)
		for i in coins:
			num_coins = func(coin_list, target - i)
			if num_coins < min_coins:
				min_coins = num_coins
	return min_coins


coins = list(map(int, input().split(' ')))
total = int(input())
print(func(coins,total))