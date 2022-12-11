N = int(input())
points = [list(map(int, input().split(' '))) for _ in range(N)]
points.append(points[0])
ans1, ans2 = 0,0

for i in range(N): ans1 += (points[i][0] * points[i + 1][1])
for i in range(N): ans2 += (points[i][1] * points[i + 1][0])

print(round(abs(ans1 - ans2) / 2, 1))