n,m = map(int, input().split(' '))
arr = list(map(str, input().split(' ')))
d = dict()
visit = dict()

def dfs_(d, target):
	q = []
	q.append(target)
	while q:
		a = q.pop()
		visit[a] = 1
		print(a,end=" ")
		for i in d[a]:
			if visit[i] == 0:
				q.append(i)


def dfs(d, target):
	visit[target] = 1
	print(target,end=" ")
	for i in d[target]:
		if visit[i] == 0:
			dfs(d,i)

for i in range(n):
	d[arr[i]] = list()
	visit[arr[i]] = 0

for i in range(m):
	input_node = input().split(' ')
	if input_node[1] not in d[input_node[0]]:
		d[input_node[0]].append(input_node[1])
	if input_node[0] not in d[input_node[1]]:
		d[input_node[1]].append(input_node[0])
target = input()

for i in d.keys():
	d[i].sort(reverse=True)
dfs_(d,target)