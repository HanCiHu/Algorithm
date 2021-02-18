from collections import deque

def dfs(tree, tree_root, N, depth):
	visited = {}
	for i in tree.keys():
		visited[i] = False

	q = deque()
	q.append(tree_root)

	while q:
		p = q.popleft()
		visited[p] = True
		for i in tree[p]:
			if i != '.' and visited[i] == False:
				q.append(i)
				depth[i] = depth[p] + 1

def find_parent(tree, child):
	for i in tree.keys():
		if tree[i][0] == child or tree[i][1] == child:
			return i

def search_lca(depth, findA, findB, tree):
	depthA = depth[findA]
	depthB = depth[findB]
	if depthA < depthB:
		depthA, depthB = depthB, depthA
		findA, findB = findB, findA
	level_diff = depthA - depthB

	b = 0
	while findA != findB:
		if level_diff > 0:
			for _ in range(level_diff):
				findA = find_parent(tree, findA)
			level_diff = 0
		else:
			findA = find_parent(tree, findA)
			findB = find_parent(tree, findB)
	return findB

n = int(input())
tree = {}
visit = {}
depth = {}

for _ in range(n):
	root, left, right = input().split(' ')
	tree[root] = (left, right)
	visit[root] = 0
	depth[root] = 0

findA, findB = input().split(' ')

for i in tree.keys():
	if tree[i][0] != '.':
		visit[tree[i][0]] = 1
	if tree[i][1] != '.':
		visit[tree[i][1]] = 1

tree_root = '0'

for i in visit.keys():
	if visit[i] == 0:
		tree_root = i

dfs(tree, tree_root, n, depth)
print(search_lca(depth, findA, findB, tree))