N, L = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
tree = [0] * (N*2)

def init():
  for i in range(N):
    tree[N+i] = arr[i]
  for i in range(N-1, 0, -1):
    tree[i] = min(tree[i*2], tree[i*2+1])

def update(idx, val):
  idx += N
  tree[idx] = val
  while idx > 1:
    idx //= 2
    tree[idx] = min(tree[idx*2], tree[idx*2+1])

def query(left, right):
  left += N
  right += N
  ret = 10**9
  while left < right:
    if left % 2 == 1:
      ret = min(ret, tree[left])
      left += 1
    if right % 2 == 1:
      right -= 1
      ret = min(ret, tree[right])
    left //= 2
    right //= 2
  return ret

init()

for i in range(N):
  if i-L+1 < 0: print(query(0, i+1), end=' ')
  else : print(query(i-L+1, i+1), end=' ')