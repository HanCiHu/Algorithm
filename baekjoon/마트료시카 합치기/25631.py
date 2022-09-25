from collections import deque

N = int(input())
M = list(map(int, input().split(' ')))

M = deque(sorted(M, reverse=True))
ans = 0

global largest

while M:
  largest = M.popleft()
  def func(num):
    global largest
    if largest > num:
      largest = num
      return False
    return True
  M = deque((filter(func , M)))
  ans += 1

print(ans)