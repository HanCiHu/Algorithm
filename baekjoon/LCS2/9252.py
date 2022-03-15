str1 = input()
str2 = input()

l1 = len(str1)
l2 = len(str2)

matrix = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
answer = []

m = 0
for i in range(1, l2 + 1):
	for j in range(1, l1 + 1):
		if str1[j - 1] == str2[i - 1]:
			matrix[i][j] = matrix[i - 1][j - 1] + 1
		else:
			matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])

s = ''

while len(s) != matrix[-1][-1]:
	if matrix[l2][l1] == matrix[l2 - 1][l1]:
		l2 -= 1
	elif matrix[l2][l1] == matrix[l2][l1 - 1]:
		l1 -= 1
	else:
		s += str2[l2 - 1]
		l2 -= 1
		l1 -= 1

if len(s) > 0:
	print(s[::-1])