n = int(input())

f = 1

for i in range(2, n + 1):
  f *= i
  while True:
    if f % 10 == 0:
      f //= 10
    else: break
  f %= 10000000000000000
print(str(f)[-5:])
