from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split(' ')))

length = [0]

for i in arr:
  if i > length[-1]: length.append(i)
  else: length[bisect_left(length, i)] = i

print(len(length) - 1)
