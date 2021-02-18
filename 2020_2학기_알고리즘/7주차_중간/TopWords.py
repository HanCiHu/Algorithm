import sys

k = int(input())

arr = []
d = dict()
keys = []
for i in sys.stdin:
	arr.append(i.lower().split(" "))

for i in arr:
	for j in i:
		if j not in d:
			d[j] = 1
		else:
			d[j] += 1

for i in d.keys():
	a = [i,d[i]]
	keys.append(a)

keys.sort(key=lambda x : (-int(x[1]), x[0]))

for i in range(k):
	print(keys[i][0])