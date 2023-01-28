import sys; input = sys.stdin.readline

N = int(input())
tree = [0 for _ in range(3000001)]

def update(i, left, right, taste, diff):
  if left > taste or right < taste: return
  tree[i] += diff

  if left == right: return

  update(i*2, left, (left + right) // 2, taste, diff)
  update(i*2 + 1, (left + right) // 2 + 1, right, taste, diff)

def query(i, left, right, target):
  if left == right: return left
  if tree[i] >= target:
    if tree[i * 2] < target:
      return query(i * 2 + 1, (left + right) // 2 + 1, right, target - tree[i * 2])
    else:
      return query(i * 2, left, (left + right) // 2, target)

for _ in range(N):
  cmd = list(map(int, input().split(' ')))

  if cmd[0] == 1:
    t = query(1, 1, 1000000, cmd[1])
    print(t)
    update(1, 1, 1000000, t, -1)

  elif cmd[0] == 2:
    update(1, 1, 1000000, cmd[1], cmd[2])