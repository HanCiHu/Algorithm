def check(s):
  if s == '1': return True
  if len(s) == 3:
    return s[1] == '1' or (s[0] == '0' and s[2] == '0')
  l = len(s) // 2
  if s[l] == '0':
    return sum(map(int, s)) == 0
  return s[l] == '1' and check(s[0:l]) and check(s[l + 1:len(s)])

def solution(numbers):
  answer = []
  bins = [1, 3, 7, 15, 31, 63]
  for n in numbers:
    b = format(n, 'b')
    for bnum in bins:
      if bnum >= len(b):
        b = (bnum - len(b)) * '0' + b
        break
    answer.append(1 if check(b) else 0)
  return answer

print(solution([1, 2, 3, 7, 42, 5, 111, 64, 56, 3712]))
