n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def check_square(grid, i, j) :
    a = grid[i][j] + grid[i][j+1] + grid[i+1][j]
    b = grid[i][j] + grid[i+1][j] + grid[i+1][j+1]
    c = grid[i][j] + grid[i][j+1] + grid[i+1][j+1]
    d = grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
    return max(a, b, c, d)

def check_w(grid, i, j) :
    return grid[i][j] + grid[i][j+1] + grid[i][j+2]

def check_h(grid, i, j) :
    return grid[i][j] + grid[i+1][j] + grid[i+2][j]

answer = 0

for i in range(n-1) :
    for j in range(m-1) :
        tmp = check_square(grid, i, j)
        answer = max(answer, tmp)

for i in range(n) :
    for j in range(m-2) :
        tmp = check_w(grid, i, j)
        answer = max(answer, tmp)


for i in range(n-2) :
    for j in range(m) :
        tmp2 = check_h(grid, i, j)
        answer = max(answer, tmp2)
print(answer)