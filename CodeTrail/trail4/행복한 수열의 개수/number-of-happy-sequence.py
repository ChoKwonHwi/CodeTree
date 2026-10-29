n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


answer = 0
for i in range(n) :
    cnt = 1
    for j in range(n) :
        if j == 0 :
            if cnt == m :
                answer += 1
                break
            else :
                continue
        if grid[i][j-1] == grid[i][j] :
            cnt += 1
        else :
            cnt = 1
        if cnt == m :
            answer += 1
            break

for i in range(n) :
    cnt = 1
    for j in range(n) :
        if j == 0 :
            if cnt == m :
                answer += 1
                break
            else :
                continue
        if grid[j-1][i] == grid[j][i] :
            cnt += 1
        else :
            cnt = 1
        if cnt == m :
            answer += 1
            break
print(answer)