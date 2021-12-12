n = int(input())
lst = list(map(int, input().split(' ')))
lst2 = list(sorted(set(lst)))
d = dict()
for i in range(len(lst2)):
	d[lst2[i]] = i
for i in lst:
	print(d[i])