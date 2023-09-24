from bisect import bisect_left

N, M, P = map(int, input().split())
main_dish = list(map(int, input().split()))
side_dish = list(map(int, input().split()))

main_dish.sort()
side_dish.sort()

side_dish_acc = [0]
cnt = 0 
for s in side_dish:
  cnt += s
  side_dish_acc.append(cnt)

ans = 0

for i in main_dish:
  find = bisect_left(side_dish, P - i)
  ans += (i * find) + side_dish_acc[find]
  ans += P * (M - find)

print(ans)
