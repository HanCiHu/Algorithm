import heapq

def dijkstra(edges, V, E, src, dst):
	INF = float('inf')
	distance = {}
	found = {}
	route = {}
	for i in edges.keys():
		distance[i] = INF
		found[i] = False
	distance[src] = 0
	queue = []

	heapq.heappush(queue, [0, src])

	while queue:
		v = heapq.heappop(queue)
		found[v[1]] = True
		for node_weight in edges[v[1]]:
			if (found[node_weight[0]]): continue
			if (distance[node_weight[0]] > distance[v[1]] + node_weight[1]):
				distance[node_weight[0]] = distance[v[1]] + node_weight[1]
				heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])
				route[node_weight[0]] = [v[1], node_weight[1]]

	node = dst
	ans = []

	while node != src:
		ans.append([node, route[node][0], route[node][1]])
		node = route[node][0]

	for i in range(len(ans) - 1, -1 ,-1):
		print(ans[i][1], ans[i][0], ans[i][2])
	return

V, E = map(int, input().split(' '))
nodes = input().split(' ')

edges = {}

for i in nodes:
	edges[i] = []

for _ in range(E):
	start, end, value = map(str, input().split(' '))
	edges[start].append([end, int(value)])

src, dst = input().split(' ')

dijkstra(edges,V,E,src,dst)