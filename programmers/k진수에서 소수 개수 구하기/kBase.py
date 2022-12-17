from collections import deque
from math import sqrt
from functools import reduce

def baseK(n, k):
  num_arr = deque()
  while n > 0:
    num_arr.appendleft(str(n % k))
    n = n // k
  return list(num_arr)

def isPrime(n):
  if n == 1 or n == 0: return False
  k = round(sqrt(n))
  for i in range(2, k + 1, 1):
    if n % i == 0:
      return False
  return True

def solution(n, k):
    num_arr = baseK(n, k)
    num_arr.append('0')
    past = 0
    cnt = 0
    for i in range(len(num_arr)):
      if num_arr[i] == '0':
        num = num_arr[past : i]
        if isPrime(reduce(lambda acc, cur: int(acc) * 10 + int(cur), num, 0)): cnt += 1
        past = i
    return cnt

print(solution(110011, 10))
