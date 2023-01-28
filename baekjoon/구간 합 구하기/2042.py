N, M, K = map(int, input().split(' '))
arr = [0] + [int(input()) for _ in range(N)]
tree = [0 for _ in range(3000000)]

def init(i, left, right):
  if left == right:
    tree[i] = arr[left]
    return tree[i]
  tree[i] = init(i*2, left, (left + right) // 2) + init(i*2 + 1, (left + right) // 2 + 1, right)
  return tree[i]

def update(i, left, right, target_index, diff):
  if left > target_index or right < target_index: return 0

  tree[i] += diff
  if left == right: return 0

  update(i*2, left, (left + right) // 2, target_index, diff)
  update(i*2 + 1, (left + right) // 2 + 1, right, target_index, diff)

def query(i, left, right, start, end):
  if left >= start and right <= end: return tree[i]
  if left > end or right < start: return 0
  return query(i*2, left, (left + right) // 2, start, end) + query(i*2 + 1, (left + right) // 2 + 1, right, start, end)

init(1, 1, N)

for _ in range(M + K):
  cmd = list(map(int, input().split(' ')))
  if cmd[0] == 1:
    update(1, 1, N, cmd[1], cmd[2] - arr[cmd[1]])
    arr[cmd[1]] = cmd[2]
  elif cmd[0] == 2:
    print(query(1, 1, N, cmd[1], cmd[2]))