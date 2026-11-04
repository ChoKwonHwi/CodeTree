n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

# 우-하-좌-상
dx = [1, 0, -1, 0] 
dy = [0, -1, 0, 1]

def cal_mean(tmp_a, r, c) :
    cnt = 1
    tmp = tmp_a[r][c]
    for x, y in zip(dx, dy) :
        nx, ny = c+x, r+y
        if 0 <= nx < m and 0 <= ny < n:
            cnt += 1
            tmp += tmp_a[ny][nx]
    return tmp // cnt
    

for r1, c1, r2, c2 in winds :
    top, left = r1 - 1, c1 - 1
    bottom, right = r2 - 1, c2 - 1

    tmp = a[top][left]

    for r in range(top, bottom):
        a[r][left] = a[r + 1][left]

    a[bottom][left:right] = a[bottom][left + 1:right + 1]

    for r in range(bottom, top, -1):
        a[r][right] = a[r - 1][right]

    a[top][left + 1:right + 1] = [tmp] + a[top][left + 1:right]

    tmp_a = [row[:] for row in a]

    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            a[r][c] = cal_mean(tmp_a, r, c)
        


for i in range(n) :
    print(*a[i])