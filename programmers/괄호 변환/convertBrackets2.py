def check(p):
  stack = []
  for i in p:
    if i == ')':
      if len(stack) == 0: return False
      stack.pop()
    else: stack.append("(")
  return True

def reverse(s):
  return ''.join(map(lambda x: '(' if x == ')' else ')', s))

def solution(p):
  if p == '': return ''
  count = 0
  for i in range(len(p)):
    if p[i] == '(': count += 1
    else: count -= 1
    if count == 0:
      u, v = p[:i + 1], p[i + 1:]
      if check(u): return u + solution(v)
      else:
        return '(' + solution(v) + ')' + reverse(u[1:-1])

print(solution('(()())()'))
print(solution(')('))

print(solution('()))((()'))
