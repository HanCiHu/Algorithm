from collections import defaultdict
from itertools import permutations

N,M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
output = []

for c in permutations(arr, M): output.append(c)
output = sorted(list(set(output)))

for c in output: print(' '.join(map(str, c)))
