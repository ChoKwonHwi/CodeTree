n, m, r, c = map(int, input().split())
r, c = r-1, c-1
grid = [[0] * n for _ in range(n)]

bomb = set()
bomb.add((r, c))
grid[r][c] = 1

def is_range(nx, ny) :
    return 0 <= nx < n and 0 <= ny < n

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, m+1) :
    for x, y in list(bomb) :
        for i in range(4) :
            dist = 2**(t-1)
            nx, ny = x + dist*dx[i], y + dist*dy[i]
            if is_range(nx, ny) and grid[nx][ny] == 0 :
                grid[nx][ny] = t
                bomb.add((nx, ny))
print(len(bomb))


