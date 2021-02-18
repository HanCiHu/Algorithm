import math
a,b,c = map(int, input().split())
n = a + b + c
ret = math.factorial(2*n) // (math.factorial(n) * math.factorial(n + 1))
print((ret * math.factorial(n)) // (math.factorial(a) * math.factorial(b) * math.factorial(c)))
