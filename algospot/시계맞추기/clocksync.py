C = int(input())

switch = [[0,1,2], [3, 7, 9, 11], 
[4, 10, 14, 15], [0, 4, 5, 6, 7], 
[6, 7, 8, 10, 12], [0, 2, 14, 15],
[3, 14, 15],[4, 5, 7, 14, 15],
[1, 2, 3, 4, 5],[3, 4, 5, 9, 13]]

INF = 1000

def push(clocks, switchIdx):
	for i in switch[switchIdx]:
		clocks[i] += 3
		if clocks[i] >= 15:
			clocks[i] = 3

def checkClcock(clocks):
	for hour in clocks:
		if (hour != 12):
			return False
	return True

def solve(clocks, switchIdx):
	if switchIdx == 10:
		if checkClcock(clocks):
			return 0
		return INF
	minCount = INF
	for i in range(4):
		minCount = min(i + solve(clocks, switchIdx + 1), minCount)
		push(clocks, switchIdx)

	return minCount

for _ in range(C):
	clocks = list(map(int, input().split()))
	count = solve(clocks, 0)
	print(-1 if count == INF else count)
