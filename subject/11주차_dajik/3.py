import heapq

def dijkstra(edges, V, E, src, dst,dis):
	INF = float('inf')
	distance = {}
	found = {}
	for i in edges.keys():
		distance[i] = INF
		found[i] = False
	distance[src] = 0
	queue = []
	ans = {}
	heapq.heappush(queue, [0, src])

	while queue:
		v = heapq.heappop(queue)
		found[v[1]] = True
		for node_weight in edges[v[1]]:
			if (found[node_weight[0]]): continue
			if (distance[node_weight[0]] > distance[v[1]] + node_weight[1]):
				distance[node_weight[0]] = distance[v[1]] + node_weight[1]
				heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])
				ans[node_weight[0]] = distance[node_weight[0]]

	ret = 0
	for i in ans.keys():
		if dis >= ans[i]:
			ret += 1

	return ret + 1

V, E = map(int, input().split(' '))
nodes = input().split(' ')

edges = {}
ans = {}

for i in nodes:
	edges[i] = []

for _ in range(E):
	start, end, value = map(str, input().split(' '))
	edges[start].append([end, int(value)])
	edges[end].append([start, int(value)])

dis = int(input())
for i in nodes:
	ans[i] = dijkstra(edges,V,E,i, nodes[0],dis)

max = 0
max_node = ''
for i in ans.keys():
	if max < ans[i]:
		max_node = i
		max = ans[i]

print(max_node,max)
