n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(nx, ny) :
    return 0 <= nx < n and 0 <= ny < n

for round in range(m) :
    for number in range(1, n*n+1) :
        is_find = False
        tmp = 0
        for x in range(n) :
            for y in range(n) :
                if grid[x][y] == number :
                    for dir in range(8) :
                        nx, ny = x + dx[dir], y + dy[dir]
                        if in_range(nx, ny) and tmp < grid[nx][ny] :
                            tmp = grid[nx][ny]
                            tmpx, tmpy = nx, ny
                    is_find = True
                    grid[x][y], grid[tmpx][tmpy] = grid[tmpx][tmpy], grid[x][y]
                    break
            if is_find :
                break
for i in range(n) :
    print(*grid[i])