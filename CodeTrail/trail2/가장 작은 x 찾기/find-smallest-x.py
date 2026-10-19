n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

i = 1
while True :
    x = i
    cnt = 0
    for a, b in ranges :
        x *= 2
        if a <= x <= b :
            cnt += 1
        else :
            break
    if cnt == len(ranges) :
        print(i)
        break
    i += 1