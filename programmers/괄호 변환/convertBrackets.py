def isOk(s):
  stack = []
  for i in s:
    if i == '(':
      stack.append(i)
    else:
      if len(stack) == 0:
        return False
      else:
        stack.pop()
  return True

def func(p):
  if p == '':
    return ""
  a,b = 0,0
  u,v = "", ""
  answer = ""
  for i in range(len(p)):
    if p[i] == '(': a += 1
    elif p[i] == ')': b += 1
    if a == b:
      [u,v] = p[0:i + 1], p[i + 1: len(p)]
      if not isOk(u):
        return'(' + func(v) + ')' + ''.join(list(map(lambda x: '(' if x == ')' else ')', u[1:len(u) - 1])))
      else:
        return u + func(v)

def solution(p):
  if isOk(p):
    return p
  answer = func(p)
  return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))