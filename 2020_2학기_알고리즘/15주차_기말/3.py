import heapq

def f(e, V, E, start, end):
        INF = float('inf')
        distance = {}
        f = {}
        route = {}

        for i in e.keys():
                distance[i] = INF
                f[i] = False

        distance[start] = 0
        q = []

        heapq.heappush(q, [0, start])

        while q:
                v = heapq.heappop(q)
                f[v[1]] = True

                for value in e[v[1]]:
                        if (f[value[0]]):
                            continue
                        if (distance[value[0]] > distance[v[1]] + value[1]):
                                distance[value[0]] = distance[v[1]] + value[1]
                                heapq.heappush(q, [distance[value[0]], value[0]])
                                route[value[0]] = [v[1], value[1]]

        node = end
        ans = []

        while node != end:
                ans.append([node, route[node][0], route[node][1]])
                node = route[node][0]

        for i in range(len(ans) - 1, -1 ,-1):
                print(ans[i][1], ans[i][0], ans[i][2])
        return

V, E, count = map(int, input().split(' '))
n = input().split(' ')

e = {}

for i in n:
        e[i] = []

for _ in range(E):
        start, end, value = map(str, input().split(' '))
        e[start].append([end, int(value)])

start, end = input().split(' ')

f(e,V,E,start,end)