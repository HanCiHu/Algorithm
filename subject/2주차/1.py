lst = list(map(int, input().split(' ')))
ans = []

ret = 0

for i in lst:
	if ret + i < i:
		ret = i
	else:
		ret += i
	ans.append(ret)
print(max(ans))
