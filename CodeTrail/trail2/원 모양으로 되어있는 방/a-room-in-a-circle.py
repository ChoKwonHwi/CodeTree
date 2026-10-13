import math
n = int(input())
a = [int(input()) for _ in range(n)]

answer = math.inf

for i in range(n) : # 시작 방
    dist = 0
    for move in range(n) :
        room = (i + move) % n
        dist += move * a[room]
    answer = min(answer, dist)
print(answer)