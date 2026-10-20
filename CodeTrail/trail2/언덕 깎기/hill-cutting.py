import math

N = int(input())
heights = [int(input()) for _ in range(N)]

min_cost = math.inf

for i in range(1, max(heights)) :
    cost = 0
    for tree in heights :
        if i <= tree <= i+17  :
            continue
        else :
            cost += (min(abs(i-tree), abs(i+17-tree)))**2
    min_cost = min(min_cost, cost)
print(min_cost)