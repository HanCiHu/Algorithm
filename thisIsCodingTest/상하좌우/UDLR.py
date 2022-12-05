n = int(input())
commands = list(input().split(' '))

x = 1
y = 1

for c in commands:
  if c == 'R' and x <= n:
    x += 1
  elif c == 'U' and y > 1:
    y -= 1
  elif c == 'L' and x > 1:
    x -= 1
  elif c == 'D' and y <= n:
    y += 1

print(y, x)