n,m = map(int, input().split(' '))
arr = list(map(str, input().split(' ')))
d = dict()

for i in range(n):
	d[arr[i]] = list()

for i in range(m):
	input_node = input().split(' ')
	if input_node[1] not in d[input_node[0]]:
		d[input_node[0]].append(input_node[1])
	if input_node[0] not in d[input_node[1]]:
		d[input_node[1]].append(input_node[0])
target = input()

print(len(d[target]))
