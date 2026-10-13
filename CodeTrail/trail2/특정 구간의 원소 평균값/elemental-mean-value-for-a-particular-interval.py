n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n) : 
    for j in range(i, n) :
        tmp = arr[i:j+1]
        if (sum(tmp)/len(tmp)) in tmp :
            cnt += 1
print(cnt)