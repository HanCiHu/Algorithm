N,M = map(int, input().split(' '))
T = set(map(int, input().split(' ')[1:]))
party = []
able = [1 for i in range(M)]

for i in range(M):
	party.append(set(map(int, input().split(' ')[1:])))

for _ in range(M):
	for i,p in enumerate(party):
		if T.intersection(p):
			able[i] = 0
			T = T.union(p)
print(sum(able))