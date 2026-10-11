n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(m)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

grid = [[0]*(n) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for point in points :
    cnt = 0
    grid[point[0]-1][point[1]-1] = 1
    for dx, dy in zip(dxs, dys) :
        nx, ny = point[0]-1 + dx, point[1]-1 + dy
        if not in_range(nx, ny) :
            continue
        if grid[nx][ny] == 1 :
            cnt += 1
    if cnt == 3 :
        print(1)
    else :
        print(0)