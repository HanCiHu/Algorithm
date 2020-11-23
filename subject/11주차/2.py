def ford(V,E,nodes,edges,src,dst):
	INF = float('inf')
	distance = {}
	route = {}
	for i in nodes:
		distance[i] = INF
		route[i] = []

	distance[src] = 0

	for _ in range(V - 1):
		for j in nodes:
			for k in edges[j]:
				if distance[j] == INF:
					continue
				if distance[k[0]] > k[1] + distance[j]:
					distance[k[0]] = k[1] + distance[j]
					route[k[0]] = [j, k[1]]

	for j in nodes:
		for k in edges[j]:
			if distance[j] == INF:
				continue
			if distance[k[0]] > k[1] + distance[j]:
				print("Negative Cycle!")
				return

	node = dst
	ans = []

	while node != src:
		ans.append([node, route[node][0], route[node][1]])
		node = route[node][0]

	for i in range(len(ans) - 1, -1 ,-1):
		print(ans[i][1], ans[i][0], ans[i][2])

V,E = map(int, input().split(' '))
nodes = list(map(str, input().split(' ')))
edges = {}

for i in nodes:
	edges[i] = []

for i in range(E):
	start, end, value = map(str, input().split(' '))
	edges[start].append([end, int(value)])

src, dst = map(str, input().split(' '))

ford(V,E,nodes,edges,src,dst)