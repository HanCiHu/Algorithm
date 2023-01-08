dis = [10,20,30,40]

ans1 = 0
ans2 = 0

def btk(users, emoticons, discounts, i, n):
  global ans1, ans2
  if i == n:
    p = 0
    money = 0
    for user_dis, price in users:
      m = 0
      for emoticon_price, emo_dis in discounts:
        if emo_dis >= user_dis:
          m += emoticon_price * (1 - (emo_dis / 100))
      if m >= price:
        p += 1
      else:
        money += m
    if ans1 < p:
      ans1 = p
      ans2 = money
    elif ans1 == p and money > ans2:
      ans2 = money
    return 
  for j in range(4):
    temp = discounts.copy()
    temp.append((emoticons[i], dis[j]))
    ans = btk(users, emoticons, temp, i + 1, n)
  return

def solution(users, emoticons):
  global ans1, ans2
  ans1 = 0
  ans2 = 0
  btk(users, emoticons, [], 0, len(emoticons))
  return [ans1, int(ans2)]

print(solution([[40, 10000], [25, 10000]]	, [7000, 9000]	))