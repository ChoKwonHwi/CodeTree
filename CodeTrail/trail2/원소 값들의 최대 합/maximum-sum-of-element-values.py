n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for start in arr : # 시작 위치
    s = 0
    idx = start
    for j in range(0, m) : # m번 움직임
        s += arr[idx-1]
        idx = arr[idx-1]
    answer = max(answer, s)
print(answer)