n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y) :
    return 1<=x<=n and 1<=y<=n

bigest = True
result = []

result.append(a[r][c])

while bigest :
    bigest = False
    for i in range(4) :
        nx, ny = r+dx[i], c+dy[i]
        if in_range(nx, ny) and a[nx][ny] > a[r][c] :
            r, c = nx, ny
            result.append(a[r][c])
            bigest = True
            break
    else:
        break
print(*result)