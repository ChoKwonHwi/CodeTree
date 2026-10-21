import math
n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

answer = max(arr[-1]*arr[-2]*arr[-3], arr[-1]*arr[0]*arr[1])
print(answer)