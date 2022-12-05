n,k = map(int, input().split(' '))

def ans1():
  ans = 0
  while n != 1:
    if n % k == 0:
      n = n // k
    else:
      n -= 1
    ans += 1
  return ans

print(ans1())
