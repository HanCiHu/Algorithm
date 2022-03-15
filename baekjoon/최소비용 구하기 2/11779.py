import heapq

N = int(input())
M = int(input())

INF = float('INF')

graph = [[] for _ in range(N + 1)]
distance = [[INF, []] for _ in range(N + 1)]

for _ in range(M):
	start, end, weight = map(int, input().split(' '))
	graph[start].append((weight, end))

start, end = map(int, input().split(' '))

distance[start][0] = 0
distance[start][1] += [start]

q = []
heapq.heappush(q, (0, start))

while q:
	weight, vertex = heapq.heappop(q)

	for w, v in graph[vertex]:
		if distance[v][0] > distance[vertex][0] + w:
			distance[v][0] = distance[vertex][0] + w
			distance[v][1] = [vertex]
			heapq.heappush(q, (distance[v][0], v))

print(distance[end][0])

answer = []

node = end

while node != start:
	
