import sys
input = sys.stdin.readline

n = int(input())

def countPair():
	student = -1
	count = 0
	for i, isVisit in enumerate(visit):
		if (not isVisit):
			student = i
			break
	if (student == -1): return 1

	for i in range(student, len(visit), 1):
		if (not visit[i] and isFriend[i][student]):
			visit[i] = visit[student] = True
			count += countPair()
			visit[i] = visit[student] = False
	return count

for _ in range(n):
	studentCount, friendsPairCount = map(int, input().split())
	visit = [False] * studentCount
	isFriend = [[False] * studentCount for _ in range(studentCount)]
	friendList = list(map(int, input().split()))

	for j in range(0, len(friendList), 2):
		isFriend[friendList[j]][friendList[j+1]] = True
		isFriend[friendList[j+1]][friendList[j]] = True
	print(countPair())