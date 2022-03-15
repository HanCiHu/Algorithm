from itertools import combinations

n, s = map(int ,input().split(' '))

lst = list(map(int, input().split(' ')))

ans = 0

for i in range(1, n + 1):
	p = list(combinations(lst, i))

	for j in p:
		if sum(j) == s:
			ans += 1

print(ans)