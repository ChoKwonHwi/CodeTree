from collections import Counter

n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(v - 1 for v in map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_range(nx, ny) :
    return 0 <= nx < n and 0 <= ny < n

for time in range(t) :
    for idx, (x, y) in enumerate(marbles):
        tmp, tmpx, tmpy = 0, x, y
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if is_range(nx, ny) and tmp <= a[nx][ny] :
                tmpx, tmpy, tmp = nx, ny, a[nx][ny]
        marbles[idx] = (tmpx, tmpy)
    counts = Counter(marbles)
    marbles = [pos for pos in marbles if counts[pos] == 1]
print(len(marbles))