import sys

input = sys.stdin.readline

T = int(input())

def match(w, s):
	pos = 0

	while pos < len(w) and pos < len(s):
		if w[pos] != '?' and s[pos] != w[pos]:
			break
		pos += 1
	if pos == len(w):
		return pos == len(s)
	if w[pos] == '*':
		for i in range(len(s) - pos):
			if (match(w[pos + 1:], s[pos + i:])):
				return True
	return False		

for _ in range(T):
	files = []
	wildCard = input()

	fileCount = int(input())

	for _ in range(fileCount):
		fileName = input()
		if match(wildCard, fileName):
			files.append(fileName)

	files.sort()
	for i in files:
		print(i.strip())
