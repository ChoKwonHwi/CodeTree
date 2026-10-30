n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

def calculate(r, c, a, b):
    total = 0
    row, col = r, c

    for direction, length in enumerate([a, b, a, b]):
        for _ in range(length):
            row += dr[direction]
            col += dc[direction]

            if not (0 <= row < n and 0 <= col < n):
                return 0

            total += grid[row][col]

    return total

answer = 0

for r in range(n):
    for c in range(n):
        for a in range(1, n):
            for b in range(1, n):
                if r - a - b < 0:
                    continue
                if c + a >= n or c - b < 0:
                    continue

                answer = max(answer, calculate(r, c, a, b))

print(answer)