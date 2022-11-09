from itertools import combinations

T = int(input())

for i in range(T):
  print(f'#{i + 1} {sorted(list(set(map(lambda x: sum(x), list(combinations(list(map(int, input().split(" "))),3))))), reverse=True)[4]}')
