C = int(input())

switch = [[0,1,2], [3, 7, 9, 11], 
[4, 10, 14, 15], [0, 4, 5, 6, 7], 
[6, 7, 8, 10, 12], [0, 2, 14, 15],
[3, 14, 15],[4, 5, 7, 14, 15],
[1, 2, 3, 4, 5],[3, 4, 5, 9, 13]]

INF = 1000

def checkClcock(clocks):
	for hour in clocks:
		if (hour != 12):
			return False
	return True

def clickSwitch(switchIdx):
	if checkClcock(clocks):
		return count
	minCount = INF
	if (switchIdx == 10):
		return minCount
	for i in range(4):
		minCount = min(clickSwitch(switchIdx + 1), count)
	return minCount

for _ in range(C):
	clocks = [map(int, input().split())]
	count = clickSwitch(0)
	print(-1 if count == INF else count)
