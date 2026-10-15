N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

min_first = min(r[0] for r in ranges)
max_second = max(r[1] for r in ranges)

def get_score(x, a, b) :
    if x < a :
        score = C
    elif x <= b :
        score = G
    else :
        score = H
    return score

answer = 0

for i in range(min_first-1, max_second+2) :
    tmp = 0
    for j in ranges :
        tmp += get_score(i, j[0], j[1])
    answer = max(answer, tmp)
print(answer)