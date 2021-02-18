from math import log2
from collections import deque

def generate_tree(tree, N):
	for _ in range(N-1):
		parent, child = map(int, input().split(' '))
		tree[child].append(parent)
		tree[parent].append(child)


def dfs(tree, parent_list, depth, N):
	visited = [False for _ in range(N+1)]
	q = deque()
	q.append(1)

	while q:
		p = q.popleft()
		visited[p] = True
		for i in tree[p]:
			if visited[i] == False:
				q.append(i)
				parent_list[i] = p
				depth[i] = depth[p]+1

def compute_exp_parent(exp_parent, N):
	logN = int(log2(N)+1)
	for i in range(1,N+1):
		for j in range(1, logN):
			exp_parent[i][j] = exp_parent[exp_parent[i][j - 1]][j - 1]


def search_lca(exp_parent, depth, N, M):
	logN = int(log2(N)+1)
	for _ in range(M):
		a, b = map(int, input().split(' '))
		if depth[a] > depth[b]:
			a,b = b,a
		level_diff = depth[a] - depth[b]
		for i in range(logN):
			if level_diff & 1 << i:
				b = exp_parent[b][i]

		if a == b:
			print(a)
			continue

		for i in range(logN-1, -1, -1):
			if exp_parent[a][i] != exp_parent[b][i]:
				a = exp_parent[a][i]
				b = exp_parent[b][i]

		print(exp_parent[b][0])

N = int(input())
tree = [[]for _ in range(N + 1)]
generate_tree(tree, N)

parent_list = [0 for i in range(N+1)]
depth = [0 for i in range(N+1)]
dfs(tree, parent_list, depth, N)

logN = (int)(log2(N)+1)
exp_parent = [[0 for _ in range(logN)] for i in range(N+1)]
for i in range(N+1):
	exp_parent[i][0] = parent_list[i]

compute_exp_parent(exp_parent,N)

M= int(input())
search_lca(exp_parent,depth, N,M)