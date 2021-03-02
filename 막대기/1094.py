a = int(input())
ans = 0
while a != 0:
    if a % 2 == 1:
        ans += 1
    a = a // 2
print(ans)