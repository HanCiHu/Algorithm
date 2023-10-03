MOD = 1000000007

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0

for i in range(0, N - 1, 1):
  for j in range(i + 1, N, 1):
    ans += (arr[j] - arr[i]) * pow(2, j - i - 1, MOD)
    ans %= MOD

print(ans)
