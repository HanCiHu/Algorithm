import math

N = int(input())
arr = [int(input()) for _ in range(N)]

ans = []

for i in range(1, N, 1): ans.append(abs(arr[i - 1] - arr[i]))

n = math.gcd(*ans)
ans = [n]
for i in range(2, n // 2 + 1, 1):
  if n % i == 0:
    ans.append(i)
    ans.append(n // i)

print(*set(sorted(ans)))