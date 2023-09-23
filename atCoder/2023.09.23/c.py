from itertools import combinations
K = int(input())
arr = [9 - i for i in range(10)]
ans = []
for i in range(1, 10, 1):
  comb = list(map(lambda x: int(''.join(map(str, x))), list(combinations(arr, i))))
  comb.sort()
  ans += comb

ans.sort()
ans.pop(0)
ans.append(9876543210)
print(ans[K - 1])