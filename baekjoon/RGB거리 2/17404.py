N = int(input())
INF = float('inf')

house = []

for i in range(N):
	r,g,b = map(int, input().split(' '))
	house.append([r,g,b])

def func(prev, i):
	if i == N - 1:
		return 0

	ans1 = func(0, i + 1) + house[i][0]
	ans2 = func(1, i + 1) + house[i][1]
	ans3 = func(2, i + 1) + house[i][2]

	if prev == 0:
		return min(ans2, ans3)
	elif prev == 1:
		return min(ans1, ans3)
	else:
		return min(ans1, ans2)

ans1 = func(0, 1) + house[0][0]
ans2 = func(1, 1) + house[0][1]
ans3 = func(2, 1) + house[0][2]

print(ans1, ans2, ans3)
