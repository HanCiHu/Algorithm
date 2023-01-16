N = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()

start = 0
end = len(arr) - 1

ans = (0, 4000000000)

while start < end:
  if abs(sum(ans)) > abs(arr[start] + arr[end]):
    ans = (arr[start], arr[end])
  if arr[start] + arr[end] >= 0: end -= 1
  else: start += 1

print(*ans)