a = input().split(' ')
b = input().split(' ')

ret = dict()

lst = []

for i in a:
	if i not in ret:
		ret[i] = 1
	else:
		ret[i] += 1

for i in b:
	ret[i] -= 1

for i in ret.keys():
	if ret[i] > 0:
		for j in range(ret[i]):
			lst.append(i)
lst.sort()
for i in lst:
	print(i)