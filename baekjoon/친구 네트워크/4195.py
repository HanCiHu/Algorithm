from collections import defaultdict

T = int(input())

def find(name):
  if name != parents[name]:
    parents[name] = find(parents[name])
  return parents[name]

def union(name1, name2):
  name1 = find(name1)
  name2 = find(name2)

  if name1 != name2:
    parents[name2] = name1
    rank[name1] += rank[name2]
  print(rank[name1])

for _ in range(T):
  N = int(input())

  parents = {}
  rank = defaultdict(lambda: 1)

  for _ in range(N):
    name1, name2 = map(str, input().split(' '))
    if parents.get(name1) == None:
      parents[name1] = name1
    if parents.get(name2) == None:
      parents[name2] = name2
    union(name1, name2)


