target = int(input())
a = list(map(int, input().split(' ')))
ret = dict()

lst = []

for i in range(len(a)):
	ret[a[i]] = i

for i in a:
	if target % i == 0:
		if target//i in ret.keys():
			lst.append(ret[i])
			lst.append(ret[target//i])

for i in range(0,len(lst),2):
	print(lst[i], lst[i + 1])