stack1 = list(input())
stack2 = []

N = int(input())

for _ in range(N):
  cmd = input()
  if cmd[0] == 'L' and len(stack1) > 0:
    stack2.append(stack1.pop())
  if cmd[0] == 'D' and len(stack2) > 0:
    stack1.append(stack2.pop())
  if cmd[0] == 'B' and len(stack1) > 0:
    stack1.pop()
  elif cmd[0] == 'P':
    s = cmd[2]
    stack1.append(s)

for i in stack1: print(i, end='')
for i in reversed(stack2): print(i, end='')