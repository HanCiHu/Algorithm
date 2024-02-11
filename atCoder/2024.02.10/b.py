N = int(input())
arr = []
for _ in range(N):
  cmd, Q = map(int, input().split())
  if cmd == 1: arr.append(Q)
  else: print(arr[len(arr) - Q])