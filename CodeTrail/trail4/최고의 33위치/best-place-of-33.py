n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def sum_grid(i, j, grid) :
    s = 0
    for x in range(i, i+3) :
        for y in range(j, j+3) :
            s += grid[x][y]
    return s

answer = 0

for i in range(n-2) :
    for j in range(n-2) :
        tmp = sum_grid(i, j, grid)
        answer = max(answer, tmp)
print(answer)
