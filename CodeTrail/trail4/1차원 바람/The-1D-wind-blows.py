n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

for r, dir in winds :
    # 첫 바람
    if dir == 'L':
        a[r-1] = [a[r-1][-1]] + a[r-1][:m-1]
    else :
        a[r-1] = a[r-1][1:] + [a[r-1][0]]

    # 위로 확인
    up_dir = dir # 이전 dir
    for i in range(1, r) :
        cnt = 0
        for j in range(m) :
            if a[r-1-i][j] != a[r-1-i+1][j] :
                cnt += 1
            else :
                if up_dir == 'L' :
                    a[r-1-i] = a[r-1-i][1:] + [a[r-1-i][0]]
                    up_dir = 'R'
                    break
                else :
                    a[r-1-i] = [a[r-1-i][-1]] + a[r-1-i][:m-1]
                    up_dir = 'L'
                    break
        if cnt == m :
            break

    #아래바람
    down_dir = dir # 이전 dir
    for i in range(1, n-r+1) :
        cnt = 0
        for j in range(m) :
            if a[r-1+i][j] != a[r-1+i-1][j] :
                cnt += 1
            else :
                if down_dir == 'L' :
                    a[r-1+i] = a[r-1+i][1:] + [a[r-1+i][0]]
                    down_dir = 'R'
                    break
                else :
                    a[r-1+i] = [a[r-1+i][-1]] + a[r-1+i][:m-1]
                    down_dir = 'L'
                    break
        if cnt == m :
            break

for i in range(n) :
    print(*a[i])