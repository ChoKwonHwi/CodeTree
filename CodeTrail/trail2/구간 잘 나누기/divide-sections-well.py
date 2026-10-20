N, M = map(int, input().split())
arr = list(map(int, input().split()))

def can_divide(limit):
    count = 1
    total = 0

    for num in arr:
        if total + num > limit:
            count += 1
            total = num
        else:
            total += num

    return count <= M

left = max(arr)
right = sum(arr)
answer = right

while left <= right:
    mid = (left + right) // 2

    if can_divide(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)