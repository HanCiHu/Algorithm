lst1 = list(map(int, input().split(' ')))
lst = list(map(int, input().split(' ')))
lst.sort()
print(abs(lst[lst1[0] - lst1[2]] - lst[lst1[1] - 1]))
