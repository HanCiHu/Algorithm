N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
	n1, n2 = map(int, input().split(' '))
	graph[n1].append(n2)
	graph[n2].append(n1)

q = [1]
parents[1] = 1

while q:
	node = q[-1]
	q.pop()

	for i in graph[node]:
		if parents[i] == 0:
			parents[i] = node
			q.append(i)

for i in range(2, N + 1):
	print(parents[i])
