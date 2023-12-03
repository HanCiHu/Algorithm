def solution(s):
  ans = len(s)
  for i in range(1, len(s), 1):
    target = s[0: i]
    count = 1
    answer = []
    for j in range(i, len(s), i):
      temp = s[j: j + i]
      if target == temp: count += 1
      else:
        answer.append((count, target))
        target = temp
        count = 1
    answer.append((count, target))
    ss = ''
    for count, string in answer:
      if count > 1: ss += str(count)
      ss += string
    ans = min(len(ss), ans)
  return ans


print(solution("aabbaccc"))
print(solution("abcabcdede"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcabcabcdededededede"))