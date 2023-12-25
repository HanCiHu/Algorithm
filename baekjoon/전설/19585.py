import sys; input = sys.stdin.readline

C, N = map(int, input().split())

colors = {}
for _ in range(C):
  now = colors
  for c in input().rstrip():
    if not c in now:
      now[c] = {}
    now = now[c]
  now[0] = 1

names = {input().strip() for i in range(N)}

Q = int(input())

teams = list(input().rstrip() for _ in range(Q))

def check(t):
  now = colors
  for i in range(len(t)):
    if 0 in now and t[i:] in names:
      return True
    if not t[i] in now:
      return False
    now = now[t[i]]
  return False

for t in teams:
  if check(t): print("Yes")
  else: print("No")
