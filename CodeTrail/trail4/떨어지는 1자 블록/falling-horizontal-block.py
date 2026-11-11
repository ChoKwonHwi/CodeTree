n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

height = 0
is_block = False
break_sig = True

while break_sig :
    for i in range(k-1, k-1+m) :
        if height == n-1 or grid[height+1][i] == 1:
            is_block = True
            break
    if is_block :
        for i in range(k-1, k-1+m) :
            grid[height][i] = 1
        break_sig = False
    height += 1

for i in range(n) :
    print(*grid[i])