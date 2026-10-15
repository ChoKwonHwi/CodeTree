k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

answer = 0

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            continue
        cnt = 0
        for grade in arr :
            if grade.index(i) < grade.index(j) :
                cnt += 1
        if cnt == k :
            answer += 1
print(answer)