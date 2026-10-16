n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def can_cover(points, lines):
    if not points:
        return True
    if lines == 0:
        return False

    x, y = points[0]

    # x좌표가 같은 점들을 세로선 하나로 덮기
    remaining_x = [(a, b) for a, b in points if a != x]

    # y좌표가 같은 점들을 가로선 하나로 덮기
    remaining_y = [(a, b) for a, b in points if b != y]

    return (
        can_cover(remaining_x, lines - 1)
        or can_cover(remaining_y, lines - 1)
    )

print(1 if can_cover(points, 3) else 0)