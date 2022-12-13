import heapq

def solution(alp, cop, problems):
    max_alp = max(list(map(lambda x: x[0], problems)))
    max_cop = max(list(map(lambda x: x[1], problems)))

    heap = [(0,alp, cop)]

    INF = 999999999
    distance = [[INF for _ in range(max_alp + 200)] for _ in range(max_cop + 200)]
    distance[alp][cop] = 0

    while heap:
        dist, a,c = heapq.heappop(heap)

        if distance[a][c] < dist: continue
        if a >= max_alp and c >= max_cop: return dist

        a = min(max_alp, a)
        c = min(max_cop, c)

        for p in problems:
            if p[0] <= a and p[1] <= c and distance[a + p[2]][c + p[3]] > dist + p[4]:
                distance[a + p[2]][c + p[3]] = dist + p[4]
                heapq.heappush(heap, (dist + p[4], a + p[2], c + p[3]))
        if distance[a + 1][c] > dist + 1:
            heapq.heappush(heap, (dist + 1, a + 1, c))
            distance[a + 1][c] = dist + 1
        if distance[a][c + 1] > dist + 1:
            heapq.heappush(heap, (dist + 1, a, c + 1))
            distance[a][c + 1] = dist + 1

    return distance[max_alp][max_cop]

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
