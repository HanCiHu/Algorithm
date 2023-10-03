MOD = 1000000007

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0

for i in range(0, N, 1):
  ans += arr[i] * (pow(2, i, MOD) - pow(2, N - i - 1, MOD))
print(ans % MOD)
