N = int(input())
seat = list(input())

answer = 0

for s in range(N):
    if seat[s] == '1':
        continue

    tmp = seat.copy()
    tmp[s] = '1'

    prev = -1
    tmp_ans = float('inf')

    for i in range(N):
        if tmp[i] == '1':
            if prev != -1:
                tmp_ans = min(tmp_ans, i - prev)
            prev = i

    answer = max(answer, tmp_ans)

print(answer)