import math

YT_Min, YT_Max = map(int, input().split(' '))
YJ_Min, YJ_Max = map(int, input().split(' '))

def is_prime_num(n):
  arr = [True for _ in range(n + 1)]
  arr[0] = False
  arr[1] = False

  for i in range(2, int(math.sqrt(n) + 1)):
    if arr[i] == True:
      j = 2

      while (i * j) <= n:
        arr[i * j] = False
        j += 1

  return arr

arr = is_prime_num(max(YT_Max, YJ_Max))

YT_Set = set()
YJ_Set = set()

for i in range(YT_Min, YT_Max + 1, 1):
  if arr[i]:
    YT_Set.add(i)

for i in range(YJ_Min, YJ_Max + 1, 1):
  if arr[i]:
    YJ_Set.add(i)

d_set = set(YT_Set) & set(YJ_Set)

dup = len(d_set)

YT_Set -= d_set
YJ_Set -= d_set

if len(YT_Set) == len(YJ_Set):
  if dup % 2 == 0:
    print('yj')
  else:
    print('yt')
elif len(YT_Set) > len(YJ_Set):
  print('yt')
else:
  print('yj')
