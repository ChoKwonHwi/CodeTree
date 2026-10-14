n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = 0

for i in range(n-2) :
    for j in range(n-1) :
        for k in range(n) :
            if x[i] == x[j] and (y[j] == y[k] or y[k] == y[i]) :
                answer = max(answer, abs(x[k]-x[j]) * (max(y[i], y[k], y[j]) - min(y[i], y[j], y[k])))
            elif x[i] == x[k] and (y[j] == y[k] or y[j] == y[i]) :
                answer = max(answer, abs(x[j]-x[k]) * (max(y[i], y[k], y[j]) - min(y[i], y[j], y[k])))
            elif x[j] == x[k] and (y[i] == y[j] or y[k] == y[i]) :
                answer = max(answer, abs(x[i]-x[j]) * (max(y[i], y[k], y[j]) - min(y[i], y[j], y[k])))

print(answer)