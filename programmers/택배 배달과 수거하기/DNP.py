def solution(cap, n, deliveries, pickups):
  answer = 0
  d = p = n - 1

  while d > -1 or p > -1:
    while d > -1 and deliveries[d] == 0: d-= 1
    while p > -1 and pickups[p] == 0: p -= 1
    ld,lp = d,p
    
    cd = cp = cap

    answer += (max(ld + 1, lp + 1) * 2)

    while d > -1:
      if cd >= deliveries[d]:
        cd -= deliveries[d]
        deliveries[d] = 0
      else:
        deliveries[d] -= cd
        ld = d
        break
      d -= 1

    while p > -1:
      if cp >= pickups[p]:
        cp -= pickups[p]
        pickups[p] = 0
      else:
        pickups[p] -= cp
        lp = p
        break
      p -= 1

  return answer

print(solution(4, 5, [1,0,3,1,2], [0,3,0,4,0]))
print(solution(2, 7, [1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))

# 랩 3 80