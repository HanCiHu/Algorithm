from collections import defaultdict

T = int(input())

def find(parents, name):
  if name != parents[name]:
    parents[name] = find(parents, parents[name])
  return parents[name]

def union(parents, cnt, name1, name2):
  name1 = find(parents, name1)
  name2 = find(parents, name2)

  if name1 != name2:
    parents[name2] = name1
    cnt[name1] = cnt[name2] + cnt[name1]
  print(cnt[name1])

for _ in range(T):
  cnt = defaultdict(lambda : 1)
  parents = {}

  N = int(input())

  for i in range(N):
    name1, name2 = map(str, input().split(' '))
    if not name1 in parents:
      parents[name1] = name1
    if not name2 in parents:
      parents[name2] = name2

    union(parents, cnt, name1, name2)
    