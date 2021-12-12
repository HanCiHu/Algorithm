from collections import deque
import sys

def acmCraft() :
	N,K = map(int, sys.stdin.readline().split(' '))
	build_time = [0]+list(map(int, sys.stdin.readline().split(' ')))
	build_order = [[]for _ in range(N+1)]
	depth = [0 for _ in range(N+1)]
	DP = [0 for _ in range(N+1)]
	for _ in range(K):
		cur, nxt = map(int, sys.stdin.readline().split(' '))
		build_order[cur].append(nxt)
		depth[nxt] += 1
	target = int(sys.stdin.readline())

	q = deque()
	for i in range(1,N+1,1):
		if depth[i] == 0:
			q.append(i)
			DP[i] = build_time[i]
	while q:
		a = q.popleft()
		for i in build_order[a]:
			depth[i] -= 1
			DP[i] = max(DP[i], DP[a]+build_time[i])
			if depth[i] == 0:
				q.append(i)
	print(DP[target])

if __name__ == "__main__":
	n = int(sys.stdin.readline())
	for _ in range(n):
		acmCraft()
