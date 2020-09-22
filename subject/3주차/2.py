lst = list(map(int, input().split(' ')))
dis = int(input())
ret = []
def func(x, ans):
	if x >= dis:
		if x == dis:
			ret.append(ans)
		return 0
	for i in range(3):
		func(x + lst[i], ans + 1)
func(0,0)
if len(ret) == 0:
	print(-1)
else:
	print(min(ret))
