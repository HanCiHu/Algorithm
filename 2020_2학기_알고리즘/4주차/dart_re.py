import re

def func(input_string):
	p = re.compile('(\d+)([a-zA-z])(\*|\#)?')
	score_list = p.findall(input_string)
	for i, score in enumerate(score_list):
		#i		: index
		#score	: list value
		print(i, score)
