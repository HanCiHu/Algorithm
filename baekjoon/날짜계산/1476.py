a,b,c = map(int, input().split())
a1 = 1
b1 = 1
c1 = 1
ans = 1
while a1 != a or b1 != b or c1 != c:
	a1 += 1
	b1 += 1
	c1 +=1
	ans += 1
	if a1 == 16:
		a1 = 1
	if b1 == 29:
		b1 = 1
	if c1 ==20:
		c1 = 1
print(ans)