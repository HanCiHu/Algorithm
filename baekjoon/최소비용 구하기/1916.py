import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = float('INF')
graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
	start,end, weight = map(int, input().split(' '))
	graph[start].append((weight, end))

start, end = map(int, input().split(' '))

hq = []
heapq.heappush(hq, (0, start))
distance[start] = 0

while hq:
	weight, vertex = heapq.heappop(hq)

	if distance[vertex] < weight: continue

	for w, v in graph[vertex]:
		if distance[v] > weight + w:
			distance[v] = weight + w
			heapq.heappush(hq, (distance[v], v))

print(distance[end])