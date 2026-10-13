import math

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]



answer = math.inf

for i in range(1, n-1) : # 건너뛰는 체크포인트
    nx, ny = x[0], y[0]
    dist = 0
    for j in range(0, n) :
        if i == j :
            continue
        dist += (abs(nx-x[j]) + abs(ny-y[j]))
        nx, ny = x[j], y[j]
    if dist < answer :
        answer = dist
print(answer)