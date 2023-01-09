dis = [10,20,30,40]

def btk(users, emoticons, discounts, i, n):
  ret = [0, 0]
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
    if ret[0] < p:
      ret[0] = p
      ret[1] = money
    elif ret[0] == p and money > ret[1]:
      ret[1] = money
    return [ret[0], ret[1]]

  for j in range(4):
    temp = discounts.copy()
    temp.append((emoticons[i], dis[j]))
    ret = max(ret, btk(users, emoticons, temp, i + 1, n))
  
  return ret

def solution(users, emoticons):
  ret = btk(users, emoticons, [], 0, len(emoticons))
  return [ret[0], int(ret[1])]

print(solution([[40, 10000], [25, 10000]]	, [7000, 9000]	))