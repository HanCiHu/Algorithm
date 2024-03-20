def get_sec(time):
  [h, m, s] = list(map(int, time.split(':')))
  return h * 60 * 60 + m * 60 + s

def get_time(number):
  hour = number // (60 * 60)
  number -= hour * 60 * 60

  minute = number // 60
  number -= minute * 60

  return f'{("00" + str(hour))[-2:]}:{("00" + str(minute))[-2:]}:{("00" + str(number))[-2:]}'

def solution(play_time, adv_time, logs):
  play_time = get_sec(play_time)
  adv_time = get_sec(adv_time)
  logs = list(map(lambda x: x.split('-'), logs))
  logs = sorted(list(map(lambda x: [get_sec(x[0]), get_sec(x[1])], logs)))

  start_log = list(map(lambda x: x[0], logs))
  end_log = list(map(lambda x: x[1], logs))

  timeline = [0 for _ in range(60 * 60 * 100)]

  for [start, end] in logs:
    timeline[start] += 1
    timeline[end] -= 1
  
  for i in range(1, len(timeline)): timeline[i] += timeline[i - 1]

  ans = sum(timeline[:adv_time])
  index = 0

  temp = ans
  for i in range(1, play_time - adv_time):
    temp -= timeline[i]
    temp += timeline[i + adv_time]
    if temp > ans: index = i + 1
    ans = max(temp, ans)

  return get_time(index)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))