import heapq

n = int(input())
heap = []

for _ in range(n):
  a,b,c = map(int, input().split(' '))
  heapq.heappush(heap, (b,c,a))

ans = [heapq.heappop(heap)[1]]

while heap:
  start, end, n = heapq.heappop(heap)
  if ans[0] <= start: heapq.heappop(ans)
  heapq.heappush(ans, end)

print(len(ans))