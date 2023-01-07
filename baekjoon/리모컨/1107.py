N = int(input())
M = int(input())

buttons = [True for _ in range(12)]
if M > 0:
  for i in list(map(int, input().split(' '))): buttons[i] = False

INF = float('inf')

channel = [INF for _ in range(1000002)]
channel[100] = 0

def check(n):
  if n == 0: return buttons[n]
  while n > 0:
    if not buttons[n % 10]: return False
    n //= 10
  return True

for i in range(0, 1000002, 1):
  if check(i): channel[i] = min(channel[i], len(str(i)))

for i in range(1, 500001, 1):
  channel[i] = min(channel[i], channel[i - 1] + 1)

for i in range(1000000, -1, -1):
  channel[i] = min(channel[i], channel[i + 1] + 1)

print(channel[N])