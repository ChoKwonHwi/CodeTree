n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

answer = 0

for s in range(1, 4) :
    stone = s
    cnt = 0
    for x, y, z in zip(a, b, c) :
        if stone == x :
            stone = y
        elif stone == y :
            stone = x
        x, y = y, x
        if stone == z :
            cnt += 1
    answer = max(answer, cnt)
print(answer)