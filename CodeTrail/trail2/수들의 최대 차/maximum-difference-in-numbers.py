N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = sorted(arr)
li = [0] * N
for i in range(N-1) :
    for j in range(i, N) :
        if arr[j] - arr[i] <= K :
            li[i] += 1
print(max(li))