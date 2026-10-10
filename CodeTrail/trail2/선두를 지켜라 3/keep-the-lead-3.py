N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

a_dist, b_dist = [0], [0]
count = 0

for i in range(N) :
    for time in range(t[i]) :
        a_dist.append(a_dist[-1]+v[i])

for i in range(M) :
    for time in range(t2[i]) :
        b_dist.append(b_dist[-1]+v2[i])

for i in range(1, len(a_dist)) :
    # a, b -> b, a -> b
    if a_dist[i-1] >= b_dist[i-1] and a_dist[i] < b_dist[i] :
        count += 1
    # a, b -> a, b -> a
    elif a_dist[i-1] <= b_dist[i-1] and a_dist[i] > b_dist[i] :
        count += 1
    # a -> a, b, b -> a, b
    elif (a_dist[i-1] < b_dist[i-1] or a_dist[i-1] > b_dist[i-1]) and a_dist[i] == b_dist[i] :
        count += 1
print(count)