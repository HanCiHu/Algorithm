N = int(input())
parts = list(map(int, input().split(' ')))
M = int(input())
finds = list(map(int, input().split(' ')))

parts.sort()

def bin_search(num):
  start = 0
  end = len(parts) - 1

  while start <= end:
    mid = (start + end) // 2

    if parts[mid] < num:
      start = mid + 1
    elif parts[mid] > num:
      end = mid - 1
    else:
      return True
  return False

for i in finds:
  if bin_search(i): print("yes", end=' ')
  else: print("no", end=' ')