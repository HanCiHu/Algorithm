n,m = map(int, input().split(' '))
d = dict()
for i in range(n):
	txt = input().split(' ')
	d[txt[0]] = txt[1]
for i  in range(m):
	net = input()
	print(d[net])