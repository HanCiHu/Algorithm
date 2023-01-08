def solution(today, terms, privacies):
  now_year, now_month, now_date = map(int, today.split('.'))
  term_map = {}
  for t in terms:
    [key, value] = t.split(' ')
    term_map[key] = int(value)

  ans = []

  for i, p in enumerate(privacies, start=1):
    dates, t = map(str, p.split(' '))
    year, month, date = map(int, dates.split('.'))
    month += term_map[t]
    if month > 12:
      year += ((month - 1) // 12)
      month = 12 if (month % 12) == 0 else (month % 12)

    if now_year > year: ans.append(i)
    elif now_year == year and now_month > month: ans.append(i)
    elif now_year == year and now_month == month and now_date >= date: ans.append(i)

  return ans

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))