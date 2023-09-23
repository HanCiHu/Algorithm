N, X = map(int, input().split())
arr = list(map(int ,input().split()))
arr.sort()

if X <= sum(arr[0:len(arr) - 1]):
  print(0)
elif 0 <= min(arr) <= X - sum(arr[1:len(arr) - 1]) <= max(arr) <= 100:
  print(X - sum(arr[1:len(arr) - 1]))
elif X <= sum(arr[1:]):
  print(max(arr))
else:
  print(-1)
