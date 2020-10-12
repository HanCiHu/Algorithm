data = list(map(int, input().split(' ')))
g = list(map(int, input().split(' ')))
ret = []
l = len(data)
for i in range(l):
	ret.append(data[i] // g[i])

min_mul = min(ret)
for i in range(l):
	print(g[i]*min_mul, end='')
	if i != l - 1:
		print(" ",end="")