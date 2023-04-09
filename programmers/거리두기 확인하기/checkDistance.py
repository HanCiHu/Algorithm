def checkDistance(place):
  for i in range(5):
    for j in range(5):
      if place[i][j] == 'P':
        if place[i][j + 1] == 'P': return 0 # 오른쪽 
        elif place[i][j + 1] != 'X' and place[i][j + 2] == 'P': return 0 # 두칸 오른쪽 
        elif place[i + 1][j] == 'P': return 0 # 아래
        elif place[i + 1][j] != 'X' and place[i + 2][j] == 'P': return 0 # 두칸 아래
        elif place[i + 1][j + 1] == 'P' and (place[i + 1][j] != 'X' or place[i][j + 1] != 'X'): return 0 # 대각 아래
        elif i > 0 and place[i - 1][j + 1] == 'P' and (place[i - 1][j] != 'X' or place[i][j + 1] != 'X'): return 0 # 대각 위
  return 1

def solution(places):
  answer = []
  for p in places:
    p.append("OOOOO")
    p.append("OOOOO")
    p = list(map(lambda x: x + "OO", p))
    answer.append(checkDistance(p))
  return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))