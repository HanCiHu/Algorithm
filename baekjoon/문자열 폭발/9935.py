string = list(input())
bomb = input()
length = len(bomb)
stack = []

for char in string:
  stack.append(char)
  if ''.join(stack[-length:]) == bomb:
    del stack[-length:]

if (len(stack) == 0):
  print("FRULA")
else:
  print(''.join(stack))