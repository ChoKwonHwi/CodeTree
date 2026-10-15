N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]
gifts.sort(key=lambda gift: gift[0] + gift[1])

answer = 0

for i in range(N):
    cost = gifts[i][0] // 2 + gifts[i][1]

    if cost > B:
        continue

    cnt = 1

    for j in range(N):
        if i == j:
            continue

        price = gifts[j][0] + gifts[j][1]

        if cost + price > B:
            break

        cost += price
        cnt += 1

    answer = max(answer, cnt)
print(answer)