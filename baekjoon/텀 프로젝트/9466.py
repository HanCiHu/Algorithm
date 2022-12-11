import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  students = [0] + list(map(int, input().split(' ')))
  visit = [False for _ in range(N + 1)]

  result = []

  def dfs(cycle, i):
    global result
    visit[i] = True
    cycle.append(i)
    n = students[i]
    if visit[n]:
      if n in cycle:
        result += cycle[cycle.index(n):]
        return
    else:
      dfs(cycle, n)
  
  for i in range(1, N + 1, 1):
    cycle = []
    if visit[i]: continue
    dfs(cycle, i)
  
  print(N - len(result))
  