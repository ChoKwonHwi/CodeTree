n = int(input())
adjacent = list(map(int, input().split())) if n >= 2 else []

if n == 1 :
    print(1)
    exit()

for i in range(1, adjacent[0]) :
    check = []
    check.append(i)
    for j in range(0, n-1) :
        if j == 0 :
            check.append(adjacent[j]-i)
        else :
            check.append(adjacent[j] - check[-1])
    
    if len(set(check)) == n :
        if all(x >= 1 for x in check):
            print(*check)
            break