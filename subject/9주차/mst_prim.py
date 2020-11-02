import heapq

def prim(edges, N):
	queue = []
	heapq.heappush(queue, [0,0,1])

	visit = [ False for _ in range(N+1)]
	result = []
	sum = 0

	while queue:
		h = heapq.heappop(queue)
		if visit[h[2]] == True:
			continue
		else:
			visit[h[2]] = True
			sum += h[0]
			result.append([h[1], h[2], h[0]])

		for e in edges[h[2]]:
			if (visit[e[0]]):
				continue
			heapq.heappush(queue, [e[1], h[2], e[0]])

	return sum, result

N = int(input())
M = int(input())

edges = [ [] for _ in range(N+1)]

for _ in range(M):
	u, v, c = map(int, input().split(' '))
	edges[u].append([v,c])
	edges[v].append([u,c])

print(prim(edges, N))