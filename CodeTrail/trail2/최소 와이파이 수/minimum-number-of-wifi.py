n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
count = 0
wifi = False

# 순회를 하면서 index를 덮는 가장 오른쪽에 wifi 설치
# wifi가 덮는 범위 다음부터 확인

answer = 0
i = 0

while i < n:
    if arr[i] == 0:
        i += 1
    else:
        location = min(i + m, n - 1)
        answer += 1
        i = location + m + 1

print(answer)