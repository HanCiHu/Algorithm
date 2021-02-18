def fib(n):
	if n <= 1:
		return 1
	else:
		fib(n - 1) + fib(n - 2)
