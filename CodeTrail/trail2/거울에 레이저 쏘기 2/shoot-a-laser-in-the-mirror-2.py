n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# 0: 아래, 1: 왼쪽, 2: 위, 3: 오른쪽
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

if k <= n:              # 위쪽: 왼쪽 → 오른쪽
    x, y = 0, k - 1
elif k <= 2 * n:        # 오른쪽: 위 → 아래
    x, y = k - n - 1, n - 1
elif k <= 3 * n:        # 아래쪽: 오른쪽 → 왼쪽
    x, y = n - 1, 3 * n - k
else:                   # 왼쪽: 아래 → 위
    x, y = 4 * n - k, 0

dir_num = (k - 1) // n
cnt = 0

while in_range(x, y) :
    if grid[x][y] == '/' :
        if dir_num == 0 or dir_num == 2 :
            dir_num = (dir_num + 1) % 4
        else :
            dir_num = (dir_num + 3) % 4
    elif grid[x][y] == "\\" :
        if dir_num == 0 or dir_num == 2 :
            dir_num = (dir_num + 3) % 4
        else :
            dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    cnt += 1
print(cnt)