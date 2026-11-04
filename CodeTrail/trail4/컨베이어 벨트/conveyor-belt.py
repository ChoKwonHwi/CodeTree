n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))


for _ in range(t):
    tmp_u, tmp_d = u[n-1], d[n-1]
    u[1:n] = u[0:n-1]
    u[0] = tmp_d
    d[1:n] = d[:n-1]
    d[0] = tmp_u

print(*u)
print(*d)