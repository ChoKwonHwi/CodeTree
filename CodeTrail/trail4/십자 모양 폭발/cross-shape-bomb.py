def check_in_grid(a, b) :
    if 0 <= a < n and 0 <= b < n :
        return True
    return False

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

r, c = r-1, c-1

bomb_size = grid[r][c]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 폭탄 터트리기
for dir in range(4) :
    a, b = r, c
    for i in range(bomb_size) :
        if check_in_grid(a, b) :
            grid[a][b] = 0
            a, b = a+dx[dir], b+dy[dir]
        else :
            break

# grid 붕괴
for i in range(n) :
    temp = []
    for j in range(n-1, -1, -1) :
        if grid[j][i] != 0 :
            temp.append(grid[j][i])
    for k in range(n-len(temp)) :
        temp.append(0)
    for k in range(n-1, -1, -1) :
        grid[k][i] = temp[n-1-k]    


for i in range(n) :
    print(*grid[i])