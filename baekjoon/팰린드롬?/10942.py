import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
m = int(input())

cache = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

def func(start, end):
  if cache[start][end] != 0: return cache[start][end]
  if end - start <= 1:
    cache[start][end] = 1 if arr[start - 1] == arr[end - 1] else -1
    return cache[start][end]

  if arr[start - 1] == arr[end - 1]:
    if end - start > 1:
      cache[start][end] = func(start + 1, end - 1)
  else: cache[start][end] = -1
  return cache[start][end]

for i in range(m):
  s,e = map(int, input().split(' '))
  print(1 if func(s, e) == 1 else 0)
