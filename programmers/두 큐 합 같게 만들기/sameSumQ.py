from collections import deque

def solution(queue1, queue2):
  queue1 = deque(queue1)
  queue2 = deque(queue2)
  s1 = sum(queue1)
  s2 = sum(queue2)

  max_len = len(queue1) * 3

  t1 = s1
  t2 = s2

  answer = 0

  while t1 != t2:
    if t1 > t2:
      a = queue1.popleft()
      queue2.append(a)
      t1 -= a
      t2 += a
    elif t1 < t2:
      a = queue2.popleft()
      queue1.append(a)
      t1 += a
      t2 -= a
    else: break
    answer += 1
    if max_len < answer: return -1

  return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 1
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 2
print(solution([1, 1]	, [1, 5])) # 3
