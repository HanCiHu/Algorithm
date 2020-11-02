parent = {}
rank = {}

def make_set(v):
	parent[v] = v
	rank[v] = 0

def find(v):
	if parent[v] != v:
		parent[v] = find(parent[v])
	return parent[v]

def union(u, v):
	root1 = find(u)
	root2 = find(v)

	if root1 != root2:
		if rank[root1] > rank[root2]:
			parent[root2] = root1
		else:
			parent[root1] = root2
			if rank[root1] == rank[root2]:
				rank[root2] += 1

def kruskal(vertex_list, edge_list):
	for u in vertex_list:
		make_set(u)
	edges = edge_list

	edges.sort()
	mst = []
	sum = 0


	for e in edges:
		cost, u, v = e
		if find(u) != find(v):
			union(u, v)
			mst.append(e)
			sum += int(cost)
	return mst,sum

def func(mstSum, edges, vertices):
	mst = mstSum[0]
	sum = mstSum[1]
	result = 0

	for i in mst:
		edges.remove(i)
		a = kruskal(vertices, edges)
		if sum != a[1]:
			result += 1
		edges.append(i)
	return result

N,M = map(int, input().split(' '))

edges = []

vertices = list(map(str, input().split(' ')))

for _ in range(M):
	u,v,c = map(str, input().split(' '))
	if (int(c),u,v) in edges or (int(c),v,u) in edges:
		continue
	edges.append((int(c), u, v))
print(func(kruskal(vertices, edges),edges, vertices))