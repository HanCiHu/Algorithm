N = int(input())
SDSD = input()

ans = 0

for i in range(0, N//2 ,1):
  if (SDSD[i] != SDSD[N - i - 1]):
    ans += 1
print(ans)