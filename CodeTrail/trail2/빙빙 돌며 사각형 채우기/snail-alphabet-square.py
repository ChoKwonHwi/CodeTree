n, m = map(int, input().split())

answer = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0 
dir_num = 0  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

answer[x][y] = 'A'

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    while not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 3) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

    x, y = nx, ny
    answer[x][y] = chr(ord('A') + (i - 1) % 26)

for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()