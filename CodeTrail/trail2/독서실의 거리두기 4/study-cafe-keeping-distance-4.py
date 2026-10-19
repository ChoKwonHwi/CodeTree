N = int(input())
seat = list(input())

answer = 0

answer = 0

for s in range(N - 1):
    if seat[s] == '1':
        continue

    for t in range(s + 1, N):
        if seat[t] == '1':
            continue

        tmp = seat.copy()
        tmp[s] = '1'
        tmp[t] = '1'

        prev = -1
        tmp_ans = float('inf')

        for i in range(N):
            if tmp[i] == '1':
                if prev != -1:
                    tmp_ans = min(tmp_ans, i - prev)
                prev = i

        answer = max(answer, tmp_ans)

print(answer)