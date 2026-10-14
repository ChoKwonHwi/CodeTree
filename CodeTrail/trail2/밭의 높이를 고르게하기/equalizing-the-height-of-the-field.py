import math

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

answer = math.inf

for i in range(N-T+1) :
    tmp = 0
    for j in range(i, i+T) :
        tmp += abs(H-arr[j])
    answer = min(answer, tmp)
print(answer)