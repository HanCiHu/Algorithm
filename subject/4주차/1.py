def func(s1, s2):
	if ''.join(sorted(s1.lower())) == ''.join(sorted(s2.lower())):
		return True
	else:
		return False

s1, s2 = map(str, input().split(' '))
print(func(s1,s2))
