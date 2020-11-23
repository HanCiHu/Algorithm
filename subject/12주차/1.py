from collections import defaultdict
V,E = map(int, input().split(' '))
subject_list = list(input().split(' '))

road_map = defaultdict(lambda : [])

for i in range(E):
	start, end = map(str, input().split(' '))
	road_map[start].append(end)

arr = []
for i in road_map.keys():
	flag = 0
	for j in road_map.keys():
		if i in road_map[j]:
			flag = 1
			break
	if flag == 0:
		arr.append(i)

ans = []
while len(arr) != 0:
	arr.sort(reverse=True)
	key = arr.pop()
	ans.append(key)
	for i in road_map[key]:
		cnt = 0
		for j in road_map.keys():
			if i in road_map[j]:
				cnt += 1
		if cnt <= 1:
			arr.append(i)
	road_map[key] = []

for i in ans:
	print(i, end=" ")
