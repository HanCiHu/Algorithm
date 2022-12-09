N, M = map(int, input().split(' '))

parents = [i for i in range(N + 1)]

def find(a):
  if parents[a] != a: parents[a] = find(parents[a])
  return parents[a]

def union(a,b):
  pa, pb = find(a), find(b)
  if pa < pb: parents[pa] = pb
  else: parents[pb] = pa

for _ in range(M):
  mode, a, b = map(int, input().split(' '))
  if mode == 0:
    union(a, b)
  elif mode == 1:
    a = find(a)
    b = find(b)
    if a == b: print("YES")
    else: print("NO")
