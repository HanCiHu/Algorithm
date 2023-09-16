S = input()

ans = 1

for i in range(len(S)):
  for j in range(i + 2, len(S) + 1, 1):
    s = S[i:j]
    if s == s[::-1]:
      ans = max(ans, len(s))

print(ans)
