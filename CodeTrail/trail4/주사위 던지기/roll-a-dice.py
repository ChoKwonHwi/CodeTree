n, m, x, y = map(int, input().split())
directions = list(input().split())

grid = [[0] * n for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [1, 5, 3, 4, 2, 6] # 0위 윗면, 5가 바닥

x, y = x-1, y-1

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 'R': #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 'L': #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 'U': #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

def is_range(nx, ny) :
    return 0<=nx<n and 0<=ny<n

grid[x][y] = dice[5]

for dir in directions :
    if dir == 'R' :
        nx, ny = x + dx[0], y + dy[0]
    elif dir == 'L' :
        nx, ny = x + dx[1], y + dy[1]
    elif dir == 'U' :
        nx, ny = x + dx[2], y + dy[2]
    else :
        nx, ny = x + dx[3], y + dy[3]
    
    if is_range(nx, ny) :
        x, y = nx, ny
        turn(dir)
        grid[x][y] = dice[5]

answer = 0
for i in range(n) :
    answer += sum(grid[i])
print(answer)