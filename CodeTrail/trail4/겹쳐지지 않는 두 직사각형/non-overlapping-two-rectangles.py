n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * (m + 1) for _ in range(n + 1)]

for r in range(n):
    for c in range(m):
        prefix[r + 1][c + 1] = (grid[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c])

def rectangle_sum(r1, c1, r2, c2):
    return (
        prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1])

NEG_INF = float('-inf')

left = [NEG_INF] * m
right = [NEG_INF] * m
top = [NEG_INF] * n
bottom = [NEG_INF] * n

for r1 in range(n):
    for r2 in range(r1, n):
        for c1 in range(m):
            for c2 in range(c1, m):
                total = rectangle_sum(r1, c1, r2, c2)
                left[c2] = max(left[c2], total)
                right[c1] = max(right[c1], total)
                top[r2] = max(top[r2], total)
                bottom[r1] = max(bottom[r1], total)

for c in range(1, m):
    left[c] = max(left[c], left[c - 1])

for c in range(m - 2, -1, -1):
    right[c] = max(right[c], right[c + 1])

for r in range(1, n):
    top[r] = max(top[r], top[r - 1])

for r in range(n - 2, -1, -1):
    bottom[r] = max(bottom[r], bottom[r + 1])

answer = NEG_INF

for c in range(m - 1):
    answer = max(answer, left[c] + right[c + 1])

for r in range(n - 1):
    answer = max(answer, top[r] + bottom[r + 1])

print(answer)