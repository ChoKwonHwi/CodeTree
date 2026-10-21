n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

a, b = 0, 0
li = [(0, 0)]
answer = 0
for i in range(1, n+1) :
    if c[i-1] == 'A' :
        a += s[i-1]
    else :
        b += s[i-1]
    li.append((a, b))
    if li[i-1][0] == li[i][0] and li[i-1][1] == li[i][1] :
        continue
    elif li[i-1][0] >= li[i-1][1] and li[i][0] <= li[i][1] :
        answer += 1
    elif li[i-1][0] <= li[i-1][1] and li[i][0] >= li[i][1] :
        answer += 1
print(answer)