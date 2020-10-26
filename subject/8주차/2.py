import queue
n,m = map(int, input().split(' '))
arr = list(map(str, input().split(' ')))
d = dict()
visit = dict()

def bfs(d,target):
	q = []
	q.append(target)
	visit[target] = 1

	while len(q) != 0:
		a = q[0]
		del q[0]
		print(a,end=" ")
		for i in d[a]:
			if visit[i] == 0:
				q.append(i)
				visit[i] = 1

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
	d[i].sort()

bfs(d,target)