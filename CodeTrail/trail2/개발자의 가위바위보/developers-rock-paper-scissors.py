N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

cnt1, cnt2 = 0, 0
wins = {(3, 2), (2, 1), (1, 3)}

for x, y in moves:
    if (x, y) in wins:
        cnt1 += 1
    elif x != y:
        cnt2 += 1

print(max(cnt1, cnt2))