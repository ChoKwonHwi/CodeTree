n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = 0

def is_range(nx, ny) :
    return 0 <= nx < n and 0 <= ny < n

for side in range (n*4) :
    dir = side//n
    i = side % n
    x = [0, i, n - 1, i][dir]
    y = [i, n - 1, i, 0][dir]
    x -= dx[dir]
    y -= dy[dir]
    cnt = 0
    while True :
        nx, ny = x + dx[dir], y + dy[dir]
        if not is_range(nx, ny) :
            cnt += 1
            answer = max(answer, cnt)
            break
        if is_range(nx, ny) and grid[nx][ny] == 0 :
            x, y = nx, ny
            cnt += 1
        elif is_range(nx, ny) and grid[nx][ny] == 1 :
            # / : 0->1 , 1->0, 2->3 , 3->2
            x, y = nx, ny
            if dir == 1 or dir == 3:
                dir = (dir + 3) % 4
                cnt += 1
            elif dir == 0 or dir == 2 :
                dir = (dir + 1) % 4
                cnt += 1
        elif is_range(nx, ny) and grid[nx][ny] == 2 :
            # \ : 0->3 , 1->2 , 2->1 , 3->0
            x, y = nx, ny
            if dir == 0 or dir == 2 :
                dir = (dir + 3) % 4
                cnt += 1
            elif dir == 1 or dir == 3 :
                dir = (dir + 1) % 4
                cnt += 1

print(answer)