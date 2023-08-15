import sys
input = sys.stdin.readline

T = int(input())

def func(arr, start):
  ans = 0
  if sum(arr) == len(arr): return 1
  for i in range(start, M):
    if not arr[friends[i * 2]] and not arr[friends[i * 2 + 1]]:
      arr[friends[i * 2]] = True
      arr[friends[i * 2 + 1]] = True
      ans += func(arr, i + 1)
      arr[friends[i * 2]] = False
      arr[friends[i * 2 + 1]] = False
  return ans

for _ in range(T):
  N,M = map(int, input().split())
  friends = list(map(int, input().split()))
  visit = [False for _ in range(N)]

  print(func(visit, 0))
