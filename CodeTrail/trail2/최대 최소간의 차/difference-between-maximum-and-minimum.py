import math

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 최솟값을 올려가며 고정한다. 단, 최솟값의 범위는 1부터 max(arr)까지
# 순회하며 변경 비용을 계산하여 더한다 -> cost += abs()
# 만약 num이 minimum보다 작으면 minimum-num
# num이 minimum보다 크고 minimum + k 사이라면 continue
# num이 minimum + k보다 크다면 minimum+k-num
# cost와 answer중 min값을 찾아 저장한다.

answer = math.inf

for minimum in range(1, max(arr)+1) :
    cost = 0
    for num in arr :
        if minimum <= num <= minimum+k :
            continue
        elif num < minimum :
            cost += abs(minimum-num)
        elif num > minimum + k :
            cost += abs(minimum + k - num)
    answer = min(answer, cost)
print(answer)