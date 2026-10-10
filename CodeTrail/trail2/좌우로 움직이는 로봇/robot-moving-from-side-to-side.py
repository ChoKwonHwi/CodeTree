n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

a_pos, b_pos = [0], [0]
count = 0

for i in range(n) :
    for time in range(t[i]) :
        if d[i] == 'L' :
            a_pos.append(a_pos[-1]-1)
        elif d[i] == 'R' :
            a_pos.append(a_pos[-1]+1)

for i in range(m) :
    for time in range(t_b[i]) :
        if d_b[i] == 'L' :
            b_pos.append(b_pos[-1]-1)
        elif d_b[i] == 'R' :
            b_pos.append(b_pos[-1]+1)

if sum(t) > sum(t_b) :
    for i in range(sum(t)-sum(t_b)) :
        b_pos.append(b_pos[-1])
elif sum(t) < sum(t_b) :
    for i in range(sum(t_b)-sum(t)) :
        a_pos.append(a_pos[-1])

for i in range(1, len(a_pos)) :
    if a_pos[i-1] != b_pos[i-1] and a_pos[i] == b_pos[i] :
        count += 1
print(count)