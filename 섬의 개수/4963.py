dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]
def bfs(i,j):
    q = [[i,j]]
    m[i][j] = 0
    while q:
        a = q[0][0]
        b = q[0][1]
        del q[0]
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w:
                if m[x][y] == 1:
                    q.append([x,y])
                    m[x][y] = 0
while True:
    ans = 0
    w, h = map(int, input().split(' '))
    if w == 0 and h == 0:
        break;
    m = []
    for i in range(h):
        m.append(list(map(int, input().split(' '))))
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                bfs(i,j)
                ans += 1
    print(ans)