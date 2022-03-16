N, M = map(int, input().split(' '))

trees = list(map(int, input().split(' ')))

left = 1
right = max(trees)

while left <= right:
  mid = (left + right) // 2

  s = 0
  for t in trees:
    if t < mid:
      continue
    s += t - mid
  if s >= M:
    left = mid + 1
  elif s < M:
    right = mid - 1

print(right)