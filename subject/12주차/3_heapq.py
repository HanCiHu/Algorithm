import heapq
import math

M,N,oil = map(int, input().split(' '))
MAP = []
visit = [[False for _ in range(N)] for i in range(M)]
for i in range(M):
	line = input()
	if line.find("S") != -1:
		start = [line.find("S"), i]
	elif line.find("E") != -1:
		end = [line.find("E"), i]
	MAP.append(line)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

class Node:
	def __init__(self,x,y, g):
		self.x = x
		self.y = y

		self.g = g
		self.h = math.sqrt( (x - end[0])**2 + (y - end[1])**2 )
		self.f = g + self.h

	def __lt__(self, other):
		return self.g < other.g

x = start[0]
y = start[1]
visit[y][x] = True

q = []
heapq.heappush(q, Node(x,y,0))
while q:
	node = heapq.heappop(q)
	x = node.x
	y = node.y
	if node.h == 0:
		break
	for i in range(4):
		if x + dx[i] >=0 and x + dx[i]< N and y + dy[i]>= 0 and y + dy[i]< M:
			if visit[y + dy[i]][x + dx[i]] == False:
				visit[y + dy[i]][x + dx[i]] = True
				if MAP[y + dy[i]][x + dx[i]] == 'E':
					heapq.heappush(q, Node(x + dx[i],y + dy[i], node.g))
				else:
					heapq.heappush(q, Node(x + dx[i],y + dy[i], node.g + int(MAP[y + dy[i]][x + dx[i]])))

if node.g <= oil:
	print(oil - node.g)
else:
	print("Not enough oil!")

