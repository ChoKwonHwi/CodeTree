n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

answer = 0

for i in range(n) :
    cal_time = [0]*1001
    for j in range(n) :
        if i == j :
            continue
        for k in range(a[j], b[j]) :
            cal_time[k] = 1
    answer = max(answer, sum(cal_time))
print(answer)