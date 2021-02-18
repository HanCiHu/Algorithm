n = int(input())
lst = list(map(int,input().split(' ')))
if n == 1:
	print(1)
else:
	print(int(n * (n - 1) / 2))
lst.sort()
for i in range(len(lst)):
	print(lst[i] ,end=" ")
