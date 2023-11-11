N = int(input())
dates = list(map(int, input().split()))
ans = 0

def check(num):
  while num >= 10:
    if num % 10 != (num // 10) % 10: return False
    num //= 10
  return True

for i in range(1, N + 1, 1):
  if check(i):
    digit = i % 10
    for j in range(1, dates[i - 1] + 1, 1):
      if check(j) and j  % 10 == digit:
        ans += 1

print(ans)
