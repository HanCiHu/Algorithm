import sys; input = sys.stdin.readline
INF = float('inf')
N, M = map(int ,input().split(' '))
arr = [int(input()) for _ in range(N)]

max_tree = [0 for _ in range(4 * N + 1)]
min_tree = [INF for _ in range(4 * N + 1)]

# mode 0 :: max
# mode 1 :: min
def init(tree, mode, i, start, end):
  if start == end:
    tree[i] = arr[start - 1]
    return tree[i]

  if mode == 0: tree[i] = max(init(tree, mode, i*2, start, (start + end) // 2), init(tree, mode, i*2 + 1, (start + end) // 2 + 1, end))
  else: tree[i] = min(init(tree, mode, i*2, start, (start + end) // 2), init(tree, mode, i*2 + 1, (start + end) // 2 + 1, end))

  return tree[i]

def query(tree, mode, i, start, end, left, right):
  if right < start or left > end: return 0 if mode == 0 else INF
  if start <= left and end >= right: return tree[i]
  if mode == 0:
    return max(query(tree, mode, i*2, start, end, left, (left + right) // 2), query(tree, mode, i * 2 + 1, start, end, (left + right) // 2 + 1, right))
  else:
    return min(query(tree, mode, i*2, start, end, left, (left + right) // 2), query(tree, mode, i * 2 + 1, start, end, (left + right) // 2 + 1, right))

init(min_tree, 1, 1, 1, N)
init(max_tree, 0, 1, 1, N)

for _ in range(M):
  a, b = map(int, input().split(' '))
  print(query(min_tree, 1, 1, a,b, 1, N), query(max_tree, 0, 1, a,b, 1, N))
