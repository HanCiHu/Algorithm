import sys

count = int(input())
total_sum = 0

for line in sys.stdin.readlines():
	total_sum += sum([int(i) for i in line.split()])
print(total_sum)
