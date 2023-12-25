N, ATK = map(int, input().split())
dungeon = [tuple(map(int, input().split())) for _ in range(N)]

start = 1
end = 1000000 * 1000000 * N

while start <= end:
  mid = (start + end) // 2
  now_atk, now_hp = ATK, mid

  for m, a, h in dungeon:
    if m == 1:
      now_hp -= (h // now_atk - 1) * a if h % now_atk == 0 else (h // now_atk) * a
    elif m == 2:
      now_hp += h
      now_atk += a
      if now_hp > mid: now_hp = mid

    if now_hp <= 0: break
  
  if now_hp > 0:
    end = mid - 1
  else:
    start = mid + 1

print(end + 1)
