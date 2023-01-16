N = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()

ans = (0, 0, 4000000000)

for i in range(N):
  tmp = (arr[i], 0, 4000000000)

  start = 0
  end = N - 1

  while start < end:
    if start == i:
      start += 1
      continue
    if end == i:
      end -= 1
      continue
    if abs(arr[i] + arr[start] + arr[end]) < abs(sum(tmp)): tmp = (arr[i], arr[start], arr[end])
    if arr[i] + arr[start] + arr[end] > 0: end -= 1
    else: start += 1
  if abs(sum(tmp)) < abs(sum(ans)): ans = tmp
print(*ans)