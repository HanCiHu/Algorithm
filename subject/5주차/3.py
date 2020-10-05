import sys
arr = list()
for line in sys.stdin:
	lst = line.split('-')
	if '-' not in line:
		lst1 = lst[0].split('.')
		lst2 = list()
		lst2.append(lst1[0])
		lst2.append("0")
		lst2.append(lst1[1])
		lst2.append(lst1[1].lower())
		arr.append(lst2)
	else:
		lst1 = lst[1].split('.')
		lst2 = list()
		lst2.append(lst[0])
		lst2.append(lst1[0])
		lst2.append(lst1[1])
		lst2.append(lst1[1].lower())
		arr.append(lst2)

arr.sort(key=lambda x: (x[3],x[0],int(x[1])))

for i in arr:
	print(i[0],end='')
	if i[1] == "0":
		print(".",end="")
		print(i[2],end="")
	else:
		print("-",end="")
		print(i[1],end="")
		print(".",end="")
		print(i[2],end="")
