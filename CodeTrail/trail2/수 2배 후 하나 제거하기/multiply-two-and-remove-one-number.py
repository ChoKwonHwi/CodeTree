import math
n = int(input())
arr = list(map(int, input().split()))

answer = math.inf

for i in range(n) :
    arr[i] = arr[i]*2

    for j in range(n):
        remaining = arr[:j] + arr[j + 1:]

        score = 0
        for k in range(n - 2):
            score += abs(remaining[k] - remaining[k + 1])

        answer = min(answer, score)
    arr[i] = arr[i]//2

print(answer)