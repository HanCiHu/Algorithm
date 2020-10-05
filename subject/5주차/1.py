import sys
arr = list()
for line in sys.stdin:
	arr.append(line)

arr.sort()
for i in arr:
	print(i,end="")
