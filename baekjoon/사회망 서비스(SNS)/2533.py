import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]

for _ in range(N - 1):
  start,end = map(int, input().split(' '))
  edges[start].append(end)
  edges[end].append(start)

dp = [[0,0] for _ in range(N + 1)]

def func(node):
  visit[node] = True

  for i in edges[node]:
    if not visit[i]:
      func(i)
      dp[node][0] += dp[i][1]
      dp[node][1] += min(dp[i][1], dp[i][0])
  dp[node][1] += 1

func(1)

print(min(dp[1][1], dp[1][0]))
