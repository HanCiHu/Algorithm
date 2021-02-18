import heapq

def fac(stock, dates, supplies, k):
	import_count = 0
	stock_heap = []
	index = 0

	while stock < k:
		for i in range(index, len(dates)):
			if dates[i] <= stock:
				heapq.heappush(stock_heap, (-supplies[i], supplies[i]))
				index = i + 1
			else:
				break
		max_amount = heapq.heappop(stock_heap)[1]
		stock += max_amount
		import_count += 1
	return import_count

i_amount = int(input())
import_date = list(map(int, input().split()))
import_amount = list(map(int, input().split()))
reg_import_date = int(input())
print(fac(i_amount,import_date, import_amount,reg_import_date))