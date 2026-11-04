n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for time in range(t):
    tmp_l, tmp_r, tmp_d = l[n-1], r[n-1], d[n-1]
    l[1:n] = l[0:n-1]
    l[0] = tmp_d
    r[1:n] = r[:n-1]
    r[0] = tmp_l
    d[1:n] = d[0:n-1]
    d[0] = tmp_r
print(*l)
print(*r)
print(*d)

