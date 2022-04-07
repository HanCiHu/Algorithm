s = input()
try:
  eval(s.replace('+', '&').replace('-','&').replace('/', '&').replace('*', '&'))
  print(int(eval(s.replace('/', '//'))))

except:
  print("ROCK")