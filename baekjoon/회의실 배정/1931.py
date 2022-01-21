N = int(input())

times = sorted([tuple(map(int, input().split(' '))) for _ in range(N)], key=lambda x : (x[1], x[0]))

ans = 0
end = 0

for s,e in times:
  if s >= end:
    ans += 1
    end = e
print(ans)