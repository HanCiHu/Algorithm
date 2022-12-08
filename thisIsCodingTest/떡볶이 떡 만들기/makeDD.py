N, M = map(int, input().split(' '))

DD = list(map(int, input().split(' ')))
DD.sort()

start = 0
end = max(DD)

result = 0

while start <= end:
  mid = (start + end) // 2

  s = sum(map(lambda x: 0 if x - mid < 0 else x - mid, DD)) 
  if s >= M:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)