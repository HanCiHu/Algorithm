a = int(input())
def an(s1,s2):
	if "".join(sorted(s1.lower())) == "".join(sorted(s2.lower())):
		return True
	else:
		return False

arr = []
visit = [0 for i in range(a)]

group = -1
lst = [[]]
for i in range(a):
	arr.append(input())

for i in range(a):
	if visit[i] == 0:
		group += 1
		lst.append(list())
		lst[group].append(arr[i])

		for j in range(i+1,a,1):
			if an(arr[i], arr[j]):
				lst[group].append(arr[j])
				visit[j] = 1
	visit[i] = 1

for i in lst:
	i.sort()

l = len(lst)
del(lst[l - 1])
lst.sort(key=lambda x : x[0])

for i in lst:
	print(len(i))