n = int(input())
arr = [0,1,1]
if n == 0:
	print(0)
elif n == 1:
	print(1)
elif n == 2:
	print(1)
else:
	for i in range(3, n+1, 1):
		arr.append(arr[i-1] +arr[i-2])
	print(arr[n])
