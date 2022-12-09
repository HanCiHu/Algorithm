N,M = map(int, input().split(' '))

parents = [i for i in range(N + 1)]

def find(a):
  if parents[a] != a: parents[a] = find(parents[a])
  return parents[a]

def union(a,b):
  a = find(a)
  b = find(b)
  if a < b: parents[b] = a
  else: parents[a] = b

edges = [list(map(int, input().split(' '))) for i in range(M)]

edges.sort(key=lambda x: x[2])

result = 0
last = 0

for [a,b,c] in edges:
  if find(a) != find(b):
    union(a,b)
    result += c
    last = c

print(result - last)
