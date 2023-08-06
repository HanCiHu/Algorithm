N = int(input())
people = list(map(int, input().split(' ')))

std = people[0]
m = max(people)

a = 0

for i in range(1, N, 1):
  if people[i] >= std: a+= 1

if a == 0: print(0)
else: print(m - std + 1)
