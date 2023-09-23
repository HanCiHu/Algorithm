N = input()
for i in range(0, len(N) - 1, 1):
  if int(N[i]) <= int(N[i + 1]):
    print("No")
    exit()
print("Yes")