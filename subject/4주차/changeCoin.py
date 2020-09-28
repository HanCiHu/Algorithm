def func(coin_list, target):
	min_coins = target
	if target in coin_list:
		return 1
	else:
		coins = list()
		for i in coin_list:
			if i <= target:
				coins.append(i)
		for i in coins:
			num_coins = 1 + func(coin_list, target - i)
			if num_coins < min_coins:
				min_coins = num_coins
	return min_coins


coin_list = list(map(int, input().split(' ')))
total = int(input())
print(func(coin_list,total))
