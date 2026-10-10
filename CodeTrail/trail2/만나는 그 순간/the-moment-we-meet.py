n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

a_pos = [0]
b_pos = [0]

#a
for i in range(n) :
    for j in range(0, t[i]) :
        if d[i] == 'R' :
            a_pos.append(a_pos[-1]+1)
        elif d[i] == 'L' :
            a_pos.append(a_pos[-1]-1)

for i in range(m) :
    for j in range(0, t2[i]) :
        if d2[i] == 'R' :
            b_pos.append(b_pos[-1]+1)
        elif d2[i] == 'L' :
            b_pos.append(b_pos[-1]-1)

min_time = min(len(a_pos), len(b_pos))

for time in range(1, min_time) :
    if a_pos[time] == b_pos[time] :
        print(time)
        exit()
print(-1)