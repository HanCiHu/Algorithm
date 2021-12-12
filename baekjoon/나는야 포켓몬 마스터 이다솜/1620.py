N,M = map(int, input().split(' '))
Ency1=dict()
Ency2=dict()
i = 1
for _ in range(N):
	name = input()
	Ency1[name] = i
	Ency2[i] = name
	i+=1
for _ in range(M):
	search = input()
	if(search.isdigit()):
		print(Ency2[int(search)])
	else:
		print(Ency1[search])
