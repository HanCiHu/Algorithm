M,N = map(int, input().split(" "))
board = [input() for _ in range(M)]
min_ = 1000
for i in range(M - 7):
	for j in range(N - 7):
		cnt = 0
		cnt2 = 0
		for y in range(8):
			for x in range(8):
				if (y+x) % 2 == 0 and board[y+i][x+j] == 'B':
					cnt += 1
				elif (y+x) % 2 == 1 and board[y+i][x+j] == 'W':
					cnt += 1
		for y in range(8):
			for x in range(8):
				if (y+x) % 2 == 0 and board[y+i][x+j] == 'W':
					cnt2 += 1
				elif (y+x) % 2 == 1 and board[y+i][x+j] == 'B':
					cnt2 += 1
		if min_ > cnt or min_ > cnt2:
			min_ = min(cnt, cnt2)
print(min_)