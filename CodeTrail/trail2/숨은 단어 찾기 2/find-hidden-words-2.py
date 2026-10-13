N, M = map(int, input().split())
arr = [input() for _ in range(N)]

def is_range(x, y) :
    return 0 <= x and x < N and 0 <= y and y < M

cnt = 0

for x in range(0, N) :
    for y in range(0, M) :
        if arr[x][y] == 'L' :
            if is_range(x+1, y) and is_range(x+2, y) and arr[x+1][y] == 'E' and arr[x+2][y] == 'E' :
                cnt += 1
            if is_range(x-1, y) and is_range(x-2, y) and arr[x-1][y] == 'E' and arr[x-2][y] == 'E' :
                cnt += 1
            if is_range(x, y+1) and is_range(x, y+2) and arr[x][y+1] == 'E' and arr[x][y+2] == 'E' :
                cnt += 1
            if is_range(x, y-1) and is_range(x, y-2) and arr[x][y-1] == 'E' and arr[x][y-2] == 'E' :
                cnt += 1
            if is_range(x+1, y+1) and is_range(x+2, y+2) and arr[x+1][y+1] == 'E' and arr[x+2][y+2] == 'E' :
                cnt += 1
            if is_range(x-1, y+1) and is_range(x-2, y+2) and arr[x-1][y+1] == 'E' and arr[x-2][y+2] == 'E' :
                cnt += 1
            if is_range(x+1, y-1) and is_range(x+2, y-2) and arr[x+1][y-1] == 'E' and arr[x+2][y-2] == 'E' :
                cnt += 1
            if is_range(x-1, y-1) and is_range(x-2, y-2) and arr[x-1][y-1] == 'E' and arr[x-2][y-2] == 'E' :
                cnt += 1
print(cnt)