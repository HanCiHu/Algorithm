N = int(input())
people = [[] for _ in range(N)]

for i in range(N):
  people[i] += [int(input())]
  people[i] += list(map(int, input().split(' ')))
  people[i] += [i + 1]

X = int(input())

bets = list(filter(lambda x: X in x[1:-1], people))
bets = list(filter(lambda x: x[0] == min(list(map(lambda x: x[0], bets))), bets)) 

print(len(bets))
print(*map(lambda x: x[-1], bets))
