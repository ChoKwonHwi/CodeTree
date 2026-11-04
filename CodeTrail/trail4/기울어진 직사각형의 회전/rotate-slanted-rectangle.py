n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
r -= 1
c -= 1

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

positions = []

for d, length in enumerate([m1, m2, m3, m4]):
    for _ in range(length):
        positions.append((r, c))
        r += dr[d]
        c += dc[d]

values = [grid[r][c] for r, c in positions]

if dir == 0:  # 반시계 방향
    values = values[-1:] + values[:-1]
else:               # 시계 방향
    values = values[1:] + values[:1]

for (r, c), value in zip(positions, values):
    grid[r][c] = value

for row in grid:
    print(*row)