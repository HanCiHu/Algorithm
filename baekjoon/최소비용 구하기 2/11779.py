import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

INF = float('INF')

graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]
path = [-1 for _ in range(N + 1)]

for _ in range(M):
	start, end, weight = map(int, input().split(' '))
	graph[start].append((weight, end))

start, end = map(int, input().split(' '))

distance[start] = 0

q = []
heapq.heappush(q, (0, start))

while q:
	weight, vertex = heapq.heappop(q)

	if weight > distance[vertex]: continue

	for w, v in graph[vertex]:
		if distance[v] > distance[vertex] + w:
			distance[v] = distance[vertex] + w
			path[v] = vertex
			heapq.heappush(q, (distance[v], v))

print(distance[end])

answer = [end]

node = end

while path[node] != -1:
	answer.append(path[node])
	node = path[node]

print(len(answer))
for i in answer[::-1]:
	print(i, end=' ')
