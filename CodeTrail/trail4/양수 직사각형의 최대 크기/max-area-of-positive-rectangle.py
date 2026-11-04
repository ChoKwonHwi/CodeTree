n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * (m + 1) for _ in range(n + 1)]

for r in range(n):
    for c in range(m):
        prefix[r + 1][c + 1] = ( (1 if grid[r][c] <= 0 else 0) + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c])

answer = -1

for r1 in range(n):
    for r2 in range(r1, n):
        for c1 in range(m):
            for c2 in range(c1, m):
                count = (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1])

                if count == 0:
                    area = (r2 - r1 + 1) * (c2 - c1 + 1)
                    answer = max(answer, area)

print(answer)