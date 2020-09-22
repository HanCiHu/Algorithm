n = int(input())
lst = [0 for _ in range(n)]
lst[0] = 2
lst[1] = 2
for i in range(2,n,1):
	lst[i] = lst[i - 1] + (lst[i - 2] // 2)
print(lst[n - 1])
