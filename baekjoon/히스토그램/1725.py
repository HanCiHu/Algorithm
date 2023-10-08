import sys; input=sys.stdin.readline;sys.setrecursionlimit(10**9)
N = int(input())
arr = [int(input()) for _ in range(N)]

tree = [0 for _ in range(N * 4)]

def init (node, start, end):
  if start == end: tree[node] = start
  else:
    init(node * 2, start, (start + end) // 2)
    init(node * 2 + 1, (start + end) // 2 + 1, end)

    if arr[tree[node * 2]] <= arr[tree[node * 2 + 1]]: tree[node] = tree[node * 2]
    else: tree[node] = tree[node * 2 + 1]

def query(node, start, end, left, right):
  if end < left or right < start: return -1
  if start >= left and end <= right: return tree[node]

  a = query(node * 2, start, (start + end) // 2, left, right)
  b = query(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

  if a == -1: return b
  if b == -1: return a
  
  if arr[a] > arr[b]: return b
  return a

def solved(left, right):
  m = query(1, 0, N - 1, left, right)
  ans = (right - left + 1) * arr[m]

  if m - 1 >= left: 
    a = solved(left, m - 1)
    if a > ans: ans = a
  if m + 1 <= right: 
    a = solved(m + 1, right)
    if a > ans: ans = a
  
  return ans

init(1, 0, N - 1)
print(solved(0, N - 1))
