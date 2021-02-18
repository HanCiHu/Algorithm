def anagram(str1, str2):
	if ''.join(sorted(str1)) == ''.join(sorted(str2)):
		return True
	else:
		return False

word1 = input().strip().lower().replace(" ","")
