import math
import sys
from functools import reduce
sys.setrecursionlimit(10**6)

def fact(n):
	n = int(input())
	for i in range(n):
		input_data = int(input())
		print(i, "|", math.factorial(input_data))

def rec_fac(n):
	if n <= 1:
		return 1
	else:
		n * rec_fac(n - 1)

def reduce_fac(n):
	return reduce(lambda x,y : x * y , range(1, n + 1))

if __name__ == "__main__":
	n = int(input())
	fact(n)
	print(rec_fac(n))
