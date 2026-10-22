arr = list(map(int, input().split()))

# 전부 다 양수면 a, b는 제일 작은 순서대로 0, 1번째 / c는 제일 마지막 - a, b
arr = sorted(arr)
print(arr[0], arr[1], arr[-1]-arr[0]-arr[1])