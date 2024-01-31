from math import inf

N,M = map(int, input().split())
dp = list(map(int, input().split()))
tree = [-inf for _ in range(N * 4)]

def update(node, left, right, index, value):
  if index < left or index > right: return
  if left == right:
    tree[node] = max(tree[node], value)
    return
  update(node * 2, left, (left + right) // 2, index, value)
  update(node * 2 + 1, (left + right) // 2 + 1, right, index, value)
  tree[node] = max(tree[node], value)

def query(node, left, right, start, end):
  if right < start or left > end: return -inf
  if left == right: return tree[node]
  if start <= left and end >= right: return tree[node]
  return max(query(node * 2, left, (left + right) // 2, start, end), query(node * 2 + 1, (left + right) // 2 + 1, right, start, end))

for i in range(0, N):
  dp[i] = max(dp[i], dp[i] + query(1, 0, N - 1, i - M, i - 1))
  update(1, 0, N - 1, i, dp[i])

print(max(dp))