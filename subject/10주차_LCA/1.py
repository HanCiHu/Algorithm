n = int(input())
tree = {}
visit = {}
for _ in range(n):
	root, left, right = input().split(' ')
	tree[root] = (left, right)
	visit[root] = 0

for i in tree.keys():
	if tree[i][0] != '.':
		visit[tree[i][0]] = 1
	if tree[i][1] != '.':
		visit[tree[i][1]] = 1

ans = 0

for i in visit.keys():
	if visit[i] == 0:
		ans = i
print(ans)