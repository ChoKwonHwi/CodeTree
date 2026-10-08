n = int(input())
arr = [int(input()) for _ in range(n)]

cnt_max = 1
cnt_now = 0

for i in range(n):
    if i == 0 or (arr[i] <= arr[i - 1]):
        cnt_now = 1
    else:
        cnt_now += 1
    if cnt_now >= cnt_max:
        cnt_max = cnt_now

print(cnt_max)