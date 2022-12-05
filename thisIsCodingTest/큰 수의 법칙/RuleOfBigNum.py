a,b,c = map(int, input().split(' '))
numArr = list(map(int, input().split(' ')))

def ans1():
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
  return ans

def ans2():
  numArr.sort()
  ans = numArr[-2] * (b // c) + numArr[-1] * (b - (b // c))
  return ans

print(ans1())
print(ans2())
