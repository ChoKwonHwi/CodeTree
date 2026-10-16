n = int(input())
h = [int(input()) for _ in range(n)]

answer = 0

for s in [0]+h :
    arr = [0] * n
    cnt = 0
    for i in range(n) :
        if s < h[i] :
            arr[i] = 1
    for i in range(n):
        if arr[i] == 1 and (i == 0 or arr[i - 1] == 0):
            cnt += 1
    answer = max(answer, cnt)
print(answer)