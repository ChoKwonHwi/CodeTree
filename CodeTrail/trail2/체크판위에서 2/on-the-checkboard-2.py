R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

color = grid[0][0]
answer = 0

for i in range(1, R-2) :
    for j in range(1, C-2) :
        if grid[i][j] != color :
            for k in range(i+1, R-1) :
                for l in range(j+1, C-1) :
                    if grid[k][l] == color and grid[k][l] != grid[R-1][C-1] :
                        answer += 1
                        continue
print(answer)