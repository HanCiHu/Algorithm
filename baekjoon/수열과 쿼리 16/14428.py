import sys; input=sys.stdin.readline

N = int(input())
arr = [[i + 1, v] for i, v in enumerate(list(map(int ,input().split())))]
query_len = int(input())

INF = float('inf')

tree = [0 for _ in range(N * 3)]

def min(a, b):
  return b if a[1] > b[1] else a

def init(i, start, end):
  if start == end:
    tree[i] = arr[start]
    return tree[i]
  tree[i] = min(init(i * 2, start ,(start+end) // 2), init(i * 2 + 1, (start+end) // 2 + 1, end))
  return tree[i]

# left right 찾는 범위
def query(i, start, end, left, right):
  if start > right or end < left: return [INF, INF]
  if left <= start and end <= right: return tree[i]
  return min(query(i * 2, start, (start + end) // 2, left ,right), query(i * 2 + 1, (start + end) // 2 + 1, end, left ,right))

def mutate(i, start, end, target_index, target_value):
  if target_index < start or target_index > end: return
  if start == end: tree[i] = target_value
  if start != end:
    mutate(i * 2, start, (start + end) // 2, target_index, target_value)
    mutate(i * 2 + 1, (start + end) // 2 + 1, end, target_index, target_value)
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])

init(1, 0, N - 1)

for _ in range(query_len):
  cmd, i, j = map(int,input().split())
  if cmd == 1:
    arr[i - 1][1] = j
    mutate(1, 0, N - 1, i - 1, arr[i - 1])
  if cmd == 2:
    print(query(1, 0, N - 1, i - 1, j - 1)[0])

