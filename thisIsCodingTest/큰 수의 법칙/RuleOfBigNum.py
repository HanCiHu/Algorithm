a,b,c = map(int, input().split(' '))
numArr = list(map(int, input().split(' ')))

ans = 0
flag = 0
numArr.sort()

for i in range(b):
  if flag < c:
    ans += numArr[-1]
    flag += 1
  else:
    ans += numArr[-2]
    flag = 0

print(ans)
