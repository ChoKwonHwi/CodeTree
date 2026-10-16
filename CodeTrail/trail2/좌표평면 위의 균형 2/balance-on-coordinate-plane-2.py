n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
'''
i < , j < : 1
i < , j > : 2
i > , j > : 3
i > , j < : 4
'''
answer = 101
for i in range(2, 102, 2) :
    for j in range(2, 102, 2) :
        tmp = [0, 0, 0, 0]
        for x, y in points :
            if i < x and j < y :
                tmp[0] += 1
            elif i < x and j > y :
                tmp[1] += 1
            elif i > x and j < y :
                tmp [2] += 1
            else :
                tmp [3] += 1
        answer = min(answer, max(tmp))
print(answer)