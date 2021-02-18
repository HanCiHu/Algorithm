def permutation(input_list):
	length = len(input_list)
	if length == 1:
		return [input_list]
	else:
		result = []
		for i in input_list:
			temp = input_list.copy()
			temp.remove(i)
			for j in permutation(temp):
				j.insert(0,i)
				if j not in result:
					result.append(j)
	return result

n = int(input())
lst = [x for x in range(1, n+1, 1)]
print(permutation(lst))
