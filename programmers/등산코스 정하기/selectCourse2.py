import heapq

inf = float('inf')

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    distance = [inf for _ in range(n + 1)]
    distance[0] = 0
    
    for [start, end, dist] in paths:
        graph[start].append((end, dist))
        graph[end].append((start, dist))
    for g in gates: graph[0].append((g, 0))
    
    q = [(-1,0, [])]
    ans = []
    
    while q:
        dist, node, path = heapq.heappop(q)
        
        if distance[node] < dist: continue
        if node in summits:
            ans.append([node, max(path)])
            continue
        
        for n, d in graph[node]:
            if d < distance[n]:
                heapq.heappush(q, (d, n, path + [d]))
                distance[n] = d

    return sorted(ans, key=lambda x: (x[1], x[0]))[0]