T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

answer = 0
for k in range(a, b+1) :
    d_n, d_s = 1002, 1002
    for ch, i in zip(c, x) :
        if ch == 'N' :
            if abs(k-i) <= d_n :
                d_n = abs(k-i)
        elif ch == 'S' :
            if abs(k-i) <= d_s :
                d_s = abs(k-i)
    if d_s <= d_n :
        answer += 1
print(answer)
#S 0 0 N 0 0 0 0 0 S
#o o x x x o o x x x