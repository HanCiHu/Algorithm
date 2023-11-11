S = input()
stack = []

for s in S:
  stack.append(s)
  if ''.join(stack[-3:]) == 'ABC':
    stack.pop()
    stack.pop()
    stack.pop()

print(''.join(stack))