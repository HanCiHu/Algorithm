import collections

def func(a, b):
	i = collections.Counter(a) - collections.Counter(b)
	return list(i.keys())

a = input().split(' ')
b = input().split(' ')
print(func(a, b))