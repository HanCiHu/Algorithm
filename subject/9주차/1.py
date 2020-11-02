import heapq

def prim(edges, nodes):
	queue = []
	heapq.heappush(queue, (0, [0, nodes[0]]))
	visit = dict()

	for i in nodes:
		visit[i] = False

	sum = 0

	while queue:
		h = heapq.heappop(queue)
		if visit[h[1][1]] == True:
			continue
		else:
			visit[h[1][1]] = True
			sum += int(h[0])

		for e in edges[h[1][1]]:
			if (visit[e[0]]):
				continue
			heapq.heappush(queue, (int(e[1]), [h[1][1], e[0]]))

	for i in visit.keys():
		if visit[i] == False:
			sum = 0
	return sum

N,M = map(int, input().split(' '))

edges = dict()

nodes = list(map(str, input().split(' ')))

for i in nodes:
	edges[i] = []

for _ in range(M):
	u, v, c = map(str, input().split(' '))
	edges[u].append([v,c])
	edges[v].append([u,c])

print(prim(edges, nodes))