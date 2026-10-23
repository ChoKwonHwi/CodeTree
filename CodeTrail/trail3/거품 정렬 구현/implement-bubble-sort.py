n = int(input())
a = list(map(int, input().split()))


for j in range(n) :
    for i in range(n-1) :
        if a[i] > a[i+1] :
            a[i], a[i+1] = a[i+1], a[i]

print(*a)