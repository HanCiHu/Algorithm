from collections import defaultdict

def solution(id_list, report, k):
  answer = []

  users = defaultdict(lambda: 0)
  mails = defaultdict(lambda: 0)
  reportList = defaultdict(lambda: [])
  reportLog = defaultdict(lambda: False)

  for r in report:
    if (reportLog[r] == True): continue
    [fromUser, toUser]= r.split(' ')
    users[toUser] += 1
    reportList[toUser].append(fromUser)
    reportLog[r] = True

  for i in id_list:
    if users[i] >= k:
      for j in reportList[i]:
        mails[j] += 1

  for i in id_list:
    answer.append(mails[i])
  return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))