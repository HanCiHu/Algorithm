import sys
arr = list()
for line in sys.stdin:
	info = list(line.split(" "))
	arr.append(info)
arr.sort(key=lambda x: (-int(x[1]),x[2],int(x[3]),x[0]))

for i in arr:
	print(i[0])
