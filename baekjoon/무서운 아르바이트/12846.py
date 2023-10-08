N = int(input())
arr = list(map(int, input().split()))
tree = [0 for _ in range(400000)]

def init(node, start, end):
  if start == end: tree[node] = start
  else:
    init(node * 2, start, (start + end) // 2)
    init(node * 2 + 1, (start + end) // 2 + 1, end)
    if arr[tree[node*2]] <= arr[tree[node*2+1]]: tree[node] = tree[node*2]
    else: tree[node] = tree[node*2+1]

def findMin(node, start, end, left, right):
  if left > end or right < start: return -1
  if left <= start and right >= end: return tree[node]
  a,b = findMin(node * 2, start, (start + end) // 2, left, right), findMin(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

  if a == -1: return b
  if b == -1: return a
  
  if arr[a] <= arr[b]: return a
  else: return b

def div(left, right):
  f = findMin(1, 0, N - 1, left, right)
  ans = (right - left + 1) * arr[f]

  if f - 1 >= left: ans = max(ans, div(left, f - 1))
  if f + 1 <= right: ans = max(ans, div(f + 1, right))

  return ans

init(1, 0, N - 1)
print(div(0, N-1))
