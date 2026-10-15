N, M, D, S = map(int, input().split())
# N명 M개 D기록 S시간

# 사람, 치즈, 시간
cheese_report = list(list(map(int, input().split())) for _ in range(D))
# 사람 시간
sick_report = list(list(map(int, input().split())) for _ in range(S))

answer = 0

for cheese in range(1, M+1) :
    possible = True

    for person, sick_time in sick_report:
        ate_before = False

        for p, m, eat_time in cheese_report:
            if p == person and m == cheese and eat_time < sick_time:
                ate_before = True
                break

        if not ate_before:
            possible = False
            break

    if possible:
        people = set()

        for p, m, eat_time in cheese_report:
            if m == cheese:
                people.add(p)

        answer = max(answer, len(people))

print(answer)