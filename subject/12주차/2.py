from collections import defaultdict, deque

INF = float('inf')

def bfs(source, sink, parent, edge):
	visited = defaultdict(lambda : 0)
	queue = deque()
	queue.append(source)
	visited[source] = 1

	while queue:
		u = queue.popleft()
		for i in edge[u]:
			capacity = edge[u][i]
			if visited[i]:
				continue
			if capacity <= 0:
				continue
			queue.append(i)
			visited[i] = 1
			parent[i] = u

	if visited[sink]:
		return 1
	else:
		return 0


def min_flow(source, sink, parent, edge):
	flow = INF
	while sink != source:
		flow = min(flow, edge[parent[sink]][sink])
		sink = parent[sink]
	return flow

def ford_fulkerson(source, sink, edge):
	parent = defaultdict(lambda : -1)
	max_flow = 0
	while bfs(source, sink, parent, edge):
		path_flow = min_flow(source, sink, parent, edge)
		max_flow += path_flow
		v = sink
		while v != source:
			u = parent[v]
			edge[u][v] -= path_flow
			edge[v][u] += path_flow
			v = parent[v]
	return max_flow

n = int(input())
visit = defaultdict(lambda : defaultdict(int))
edge = defaultdict(lambda : defaultdict(int))
creatures = []

for _ in range(n):
	size, speed = map(int, input().split(' '))
	creatures.append([size, speed])

for i in range(n):
	edge['S'][chr(i + 65)] = 2
	edge[chr(i+65)]['S'] = 2
	edge['T'][chr(i + 97)] = 1
	edge[chr(i + 97)]['T'] = 1

for i in range(n):
	for j in range(n):
		if i == j :
			continue

		if visit[chr(i + 65)][chr(j + 97)] == 1:
			continue

		if creatures[i][0] >= creatures[j][0] and creatures[i][1] >= creatures[j][1]:
			edge[chr(i + 65)][chr(j + 97)] = 1
			edge[chr(j + 97)][chr(i + 65)] = 1

		if creatures[i][0] == creatures[j][0] and creatures[i][1] == creatures[j][1]:
			visit[chr(j + 65)][chr(i + 97)] = 1
			visit[chr(i + 97)][chr(j + 65)] = 1

print(n-ford_fulkerson('S','T',edge))
