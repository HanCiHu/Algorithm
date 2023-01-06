from copy import deepcopy
from collections import deque

def solution(n, info):
  q = deque([(0, [0 for _ in range(11)])])
  ans = []
  maxGap = 0
  while q:
    now, lion = q.popleft()

    if sum(lion) == n:
      ap, lp = 0,0
      for i in range(11):
        if info[i] == 0 and lion[i] == 0: continue
        elif info[i] >= lion[i]: ap += (10 - i)
        else: lp += (10 - i)
      if ap < lp:
        gap = lp - ap
        if gap < maxGap: continue
        elif gap > maxGap:
          maxGap = gap
          ans.clear()
        ans.append(lion)

    elif sum(lion) > n:
      continue

    elif now == 10:
      tmp = deepcopy(lion)
      tmp[10] = n - sum(lion)
      q.append((-1, tmp))
    else:
      tmp = deepcopy(lion)
      tmp[now] = info[now] + 1
      q.append((now + 1, tmp))
      q.append((now + 1, deepcopy(lion)))
  return ans[-1] if len(ans) >= 1 else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
print(solution(3, [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]))
print(solution(2, [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(3, [0,0,1,0,0,0,0,0,0,1,0]))