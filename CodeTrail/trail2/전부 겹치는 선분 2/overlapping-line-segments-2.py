n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

for a, b in segments :
    count = [0] * 101
    for x, y in segments :
        if a == x and b == y :
            continue
        for i in range(x, y+1) :
            count[i] += 1
    if n-1 in count :
        print('Yes')
        exit()
print('No')