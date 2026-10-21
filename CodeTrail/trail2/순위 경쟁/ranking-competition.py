n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

A, B, C = 0, 0, 0
li = [(0, 0, 0)]
answer = 0
for i in range(1, n+1) :
    if c[i-1] == 'A' :
        A += s[i-1]
    elif c[i-1] == 'B' :
        B += s[i-1]
    else :
        C += s[i-1] 
    li.append((A, B, C))

    # 안 바뀌는 경우
    before = li[i - 1]
    after = li[i]
    
    before_top = {
        idx for idx in range(3)
        if before[idx] == max(before)
    }

    after_top = {
        idx for idx in range(3)
        if after[idx] == max(after)
    }
    if before_top != after_top:
        answer += 1
print(answer)