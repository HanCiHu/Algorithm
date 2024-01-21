N = int(input())

gool = {}
for _ in range(N):
  temp = input().split()
  temp_gool = gool
  for i in range(1, int(temp[0]) + 1):
    if not temp[i] in temp_gool:
      temp_gool[temp[i]] = {}
    temp_gool = temp_gool[temp[i]]

def func(temp, dep):
  if (len(temp.items()) == 0): return
  for key in sorted(temp.keys()):
    print('--' * dep, end='')
    print(key)
    func(temp[key], dep + 1)

func(gool, 0)
