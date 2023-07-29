N,M = map(int, input().split(' '))
seller = list(map(int, input().split(' ')))
buyer = list(map(int, input().split(' ')))

start = -1
end = 2100000000
answer = 2100000000

while start + 1 < end:
  mid = (start + end) // 2
  sCnt = len([v for v in seller if v <= mid])
  bCnt = len([v for v in buyer if v >= mid])

  if sCnt >= bCnt:
    end = mid
    answer = min(answer, mid)
  else:
    start = mid

print(answer)
