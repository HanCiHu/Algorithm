N = int(input())
arr = list(map(int, input().split()))

ans = float('inf')
temp = 0
for i in arr:
  temp += i
  ans = min(ans, temp)

if ans > 0: print(sum(arr))
else: print(sum(arr) - ans)