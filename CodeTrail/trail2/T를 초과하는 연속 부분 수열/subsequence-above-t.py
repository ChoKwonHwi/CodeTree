n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt_max = 0
cnt_now = 0

for i in range(n):
    if arr[i] <= t:
        cnt_now = 0
    else:
        cnt_now += 1
    if cnt_now >= cnt_max:
        cnt_max = cnt_now

print(cnt_max)