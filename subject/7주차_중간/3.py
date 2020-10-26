import re

p = re.compile('(//)(/)')
lst = p.findall(input())
for i in lst:
	print(i)