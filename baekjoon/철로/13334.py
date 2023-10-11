import sys; input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

L = int(input())
arr = list(filter(lambda x: (x[1] - x[0]) <= L, list(map(lambda x: (x[0], x[1]) if x[1] > x[0] else (x[1], x[0]), arr))))

ans = 0
cnt = 0

start = sorted(list(map(lambda x: x[0], arr)))
end = sorted(list(map(lambda x: x[1], arr)))

e = 0

for s in range(len(start)):
  if s > 0: cnt -= 1
  while e < len(end) and end[e] - start[s] <= L:
    cnt += 1
    e += 1
    ans = max(ans, cnt)
  
print(ans)