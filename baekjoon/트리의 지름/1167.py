V = int(input())
tree = [[] for _ in range(V + 1)]

for _ in range(V):
  arr = list(map(int, input().split()))
  node = arr[0]
  for i in range(1, len(arr), 2):
    if arr[i] == -1: continue
    tree[node].append((arr[i], arr[i + 1]))

def find_distance(n):
  stack = [(n, 0)]
  visit = [False for _ in range(V + 1)]
  visit[n] = True
  max_dist = -1
  max_node = -1
  while stack:
    node, dist = stack.pop()
    if max_dist < dist:
      max_dist = dist
      max_node = node
    for i, cost in tree[node]:
      if not visit[i]:
        stack.append((i, cost + dist))
        visit[i] = True
  
  return [max_node, max_dist]

[some_node, some_dist] = find_distance(1)
print(find_distance(some_node)[1])

