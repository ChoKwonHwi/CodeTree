import math

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

def check_rectangle(x, y) :
    return (max(x) - min(x)) * (max(y) - min(y))

answer = math.inf

for i in range(n) :
    tmp_x, tmp_y = x.copy(), y.copy()
    del tmp_x[i]
    del tmp_y[i]
    answer = min(answer, check_rectangle(tmp_x, tmp_y))
print(answer)