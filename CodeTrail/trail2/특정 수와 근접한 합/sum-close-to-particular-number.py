import math

N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = math.inf
for i in range(N) :
    for j in range(i+1, N) :
        result = min(result, abs((sum(arr)-arr[i]-arr[j])-S))

print(result)

