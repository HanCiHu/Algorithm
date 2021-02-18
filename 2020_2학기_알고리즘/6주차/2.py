target = int(input())
trees = list(map(int, input().split(' ')))
ret = 0
for i in trees:
	if i > target:
		trees.append(i//3)
		trees.append(int(i * (2/3)))
		ret += 1
print(ret)