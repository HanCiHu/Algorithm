import heapq

n,m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
heap = []
for i in a:
	heapq.heappush(heap,i)
for i in range(n - m - 1):
	heapq.heappop(heap)
print(heapq.heappop(heap))
