import re

def func(input_string):
	p = re.compile('(\d+)([a-zA-z])(\*|\#)?')
	score_list = p.findall(input_string)
	point = [0]*3
	for i, score in enumerate(score_list):
		if score[1] == 'S':
			point[i] += int(score[0])
		elif score[1] == 'D':
			point[i] = point[i] + int(score[0])**2
		elif score[1] == 'T':
			point[i] = point[i] + int(score[0])**3

	for i, score in enumerate(score_list):
		if score[2] == '#':
			if i == 2:
				point[i] *= -1
			else:
				point[i] *= -1
		elif score[2] == '*':
			if i == 2:
				point[i] *= 2
			else:
				point[i] *= 2
				point[i + 1] *= 2
	ret = 0
	for i in point:
		ret += i
	return ret

s = input()
print(func(s))
