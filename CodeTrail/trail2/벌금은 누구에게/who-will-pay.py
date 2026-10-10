N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
count = [0]*N
for t in range(M) :
    count[student[t]-1] += 1
    for cnt_idx in range(N) :
        if count[cnt_idx] == K :
            print(cnt_idx+1)
            exit()
print(-1)