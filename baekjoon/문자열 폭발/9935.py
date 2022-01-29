s = input()
bomb = input()

origin = s
s = origin.replace(bomb, '')
while s != origin:
  origin = s
  s = origin.replace(bomb, '')

if s == '':
  print("FRULA")
else:
  print(s)
