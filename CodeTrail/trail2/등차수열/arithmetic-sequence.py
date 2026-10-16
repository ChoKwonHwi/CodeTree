n = int(input())
a = list(map(int, input().split()))

ma, mi = max(a), min(a)
answer = 0

for k in range(mi+1, ma) :
    cnt = 0
    for i in range(n-1) :
        for j in range(i+1, n) :
            if k - a[j] == a[i] - k : 
                cnt += 1
    answer = max(answer, cnt)
print(answer)