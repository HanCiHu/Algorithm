a,b =map(int,input().split())
while True:
	if a==0 and b==0:
		break
	if b > a-b :
		b = a-b
	sum =1
	for i in range(1,b+1):
		sum = sum*a/i
		a-=1
	print(int(sum))
	a,b =map(int,input().split())
