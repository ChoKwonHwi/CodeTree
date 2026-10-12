n, t = map(int, input().split())
commands = input()
grid = [list(map(int, input().split())) for _ in range(n)]

# 북쪽, 동쪽, 남쪽, 서쪽
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

x, y = n // 2, n // 2
dir_num = 0  # 북쪽
result = grid[x][y]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for command in commands:
    if command == 'L':
        dir_num = (dir_num + 3) % 4

    elif command == 'R':
        dir_num = (dir_num + 1) % 4

    else:  # F
        nx = x + dxs[dir_num]
        ny = y + dys[dir_num]

        if in_range(nx, ny):
            x, y = nx, ny
            result += grid[x][y]

print(result)