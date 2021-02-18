from collections import deque

n = int(input())
t = dict()
visit = dict()
d = dict()
for i in range(n):
	root, left,right = map(str, input().split(' '))
	t[root] = (left, right)
	visit[root] = 0
	d[root] = 0
start, end = input().split(' ')

for i in t.keys():
	if t[i][0] != '.':
		visit[t[i][0]] = 1
	if t[i][1] != '.':
		visit[t[i][1]] = 1

root = 'a'

for i in t.keys():
	if visit[i] == 0:
		root = i
		break

def func(t, root, n, d):
	v = dict()
	for i in t.keys():
		v[i] = False
	q = deque()
	q.append(root)

	while q:
		a = q.popleft()
		v[a] = True
		for i in t[a]:
			if i != '.' and v[i] == False:
				q.append(i)
				d[i] = d[a] + 1
	return d

ans = []

def f(t, a):
	for i in t.keys():
		if t[i][0] == a or t[i][1] == a:
			return i

rootA = []
rootB = []

def lca(d,t,start,end):
	Dstart = d[start]
	Dend = d[end]
	if Dstart <= Dend:
		Dstart,Dend = Dend, Dstart
		start, end = end, start
	diff = Dstart - Dend
	rootA.append(start)
	rootB.append(end)
	while start != end:
		if diff > 0:
			for i in range(diff):
				start = f(t,start)
				rootA.append(start)
			diff = 0
		else:
			start = f(t,start)
			end = f(t,end)
			rootA.append(start)
			rootB.append(end)
	return end

d = func(t,root,n,d)
lca(d,t,start,end)

for i in rootA:
	print(i, end=" ")
for i in range(len(rootB) - 1):
	print(rootB[i])