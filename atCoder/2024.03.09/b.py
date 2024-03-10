import sys

lines = list(map(lambda x: int(x.strip()), sys.stdin.readlines()))

for line in lines[::-1]: print(line)