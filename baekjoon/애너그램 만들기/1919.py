from collections import defaultdict

str1 = input()
str2 = input()

d = defaultdict(lambda: [0,0])

for s in str1: d[s][0] += 1
for s in str2: d[s][1] += 1

print(sum([abs(d[i][0] - d[i][1]) for i in d]))