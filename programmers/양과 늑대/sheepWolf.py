from copy import deepcopy
from collections import deque

def solution(info, edges):
  n = len(info)
  graph = [[] for _ in range(n)]

  for s,e in edges:
    graph[s].append(e)
    graph[e].append(s)

  tmp = deepcopy(info)
  tmp[0] = -1
  visit = [False for _ in range(n)]
  q = deque([(tmp, [False for _ in range(n)], 0, 1, 0)])

  ans = 1

  while q:
    info, visit, now, s, w = q.popleft()
    if now == 0:
      ans = max(ans, s)
    for i in graph[now]:
      tmp = deepcopy(info)
      tmp[i] = -1
      v_tmp = [False for _ in range(n)]
      v_tmp[i] = True

      if info[i] == 0:
        a = [False for _ in range(n)]
        q.append((tmp, v_tmp, i, s + 1, w))
      elif info[i] == 1 and s > w + 1:
        q.append((tmp, v_tmp, i, s, w + 1))
      elif info[i] == -1 and not visit[i]:
        v_tmp = deepcopy(visit)
        v_tmp[i] = True
        q.append((info, v_tmp, i, s, w))
  return ans

print('sol: ', solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print('sol: ', solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))

# 5 5