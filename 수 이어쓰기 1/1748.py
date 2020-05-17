n = int(input())
l = len(str(n))
ans = 0
for i in range(l - 1):
    ans += 9 * (10 ** i) * (i + 1)
ans += ((n - (10 ** (l - 1))) + 1) * l
print(ans)
