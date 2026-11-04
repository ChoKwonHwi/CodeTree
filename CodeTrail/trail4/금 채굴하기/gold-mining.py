n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

gold = []

for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            gold.append((r, c))

answer = 0

max_k = 2 * (n - 1)

for r in range(n):
    for c in range(n):
        distance_count = [0] * (max_k + 1)

        for x, y in gold:
            distance = abs(r - x) + abs(c - y)
            distance_count[distance] += 1

        count = 0

        for k in range(max_k + 1):
            count += distance_count[k]
            cost = k * k + (k + 1) * (k + 1)

            if count * m >= cost:
                answer = max(answer, count)

print(answer)