from itertools import permutations

def tsp():
	n = int(input())
	input_list = list(map(int, input().split()))
	src = (input_list[0], input_list[2])
	dst = (input_list[2], input_list[3])
	point = []
	point_slice = input_list[4:]

	for i in range(0, len(point_slice), 2):
		point.append(point_slice[i],point_slice[i+1])
	min_distance = float('inf')

	for i in permutations(point):
		path = [src, *list(i), dst]
		distance = 0

		for j in range(0, len(path) - 1):
			distance += abs(path[j][0] - path[j + 1][0]) + abs(path[j][1] - path[j + 1][1])
		min_distance = distance if distance < min_distance else min_distance

	return min_distance

