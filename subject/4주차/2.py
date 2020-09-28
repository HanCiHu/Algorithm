def lps(s):
	table = [[False for i in range(len(s))]for j in range(len(s))]
	longest = 0

	for i in range(len(s)):
		for j in range(len(s) - i):
			if i < 2:
				if s[j] == s[j+i]:
					table[j][j+i] = True
					longest = i + 1
				else:
					table[j][j+i] = False
			else:
				if s[j]==s[j+i] and table[j+1][j+i-1]:
					table[j][j+i] = True
					longest = i + 1
				else:
					table[j][j+i] = False
	return longest
s = input().strip().replace(" ","").lower()
print(lps(s))
