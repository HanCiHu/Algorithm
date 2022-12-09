V, E = map(int, input().split(' '))

edges = [list(map(int, input().split(' ')))for _ in range(E)]
parents = [i for i in range(V + 1)]
edges.sort(lambda x: x[2])
def find(a):
  if parents[a] != a: parents[a] = find(parents[a])
  return parents[a]

def union(a,b):
  a = find(a)
  b = find(b)
  if a < b: parents[b] = a
  else: parents[a] = b

result = 0

for [a,b,c] in edges:
  if find(a) != find(b):
    union(a, b)
    result += c

print(result)
