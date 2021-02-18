import sys
import copy
sys.setrecursionlimit(10**6)

n,m = map(int, input().split(' '))
x = int(input())
idx = 0
arr = [[0 for _ in range(n)] for _ in range(x + 2)]

def ret():
	global idx,n
	i = 0
	while i < (n + 1) // 2:
		print(arr[idx][i],end='')
		i = i + 1
	if n % 2 == 0 :
		i = i - 1
	else:
		i =i - 2
	while i >= 0:
		print(arr[idx][i],end='')
		i -= 1
	sys.exit()

def func(j):
	global idx,n,m
	if j == (n + 1) // 2 :
		arr[idx + 1] = copy.deepcopy(arr[idx])
		if idx == x - 1:
			ret()
		idx = idx + 1
		return
	for i in range(m):
		arr[idx][j] = chr(97 + i)
		func(j + 1)

func(0)
