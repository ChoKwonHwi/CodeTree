N, K = map(int, input().split())
arr = list(map(int, input().split()))

for limit in range(max(arr[0], arr[-1]), max(arr) + 1):
    prev = 0
    possible = True

    for i in range(1, N):
        if arr[i] <= limit:
            if i - prev > K:
                possible = False
                break

            prev = i

    if possible:
        print(limit)
        break