N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P = sorted(P)
cnt = 0

for price in P :
    if B >= price :
        cnt += 1
        B -= price
    else :
        if B >= price // 2:
            cnt += 1
        break
print(cnt)