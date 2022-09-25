N = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = 0
for i in range(N):a+=b[i] if c[i] else 0
dp=[-9e999 for _ in range(N)]
for i in range(N):
  k=b[i] if c[i]==0 else -b[i]
  dp[i]=max(dp[i-1]+k,k)
print(a+max(dp))