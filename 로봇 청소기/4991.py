import sys

while True:
	width, height = map(int, sys.stdin.readline().split(' '))
	if width == 0 and height == 0:
		break
	m = []
	dust = []
	posX = 0
	posY = 0
	for i in range(height):
		line = sys.stdin.readline()
		m.append(line)
		if '*' in line:
			dust.append([line.index('*'),i])
		if 'o' in line:
			posX = line.index('o')
			posY = i

	for i in m:
		print(i,end="")
