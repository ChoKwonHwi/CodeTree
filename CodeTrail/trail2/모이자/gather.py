import math
n = int(input())
A = list(map(int, input().split()))

answer = math.inf

for i in range(0, n) :
    tmp = 0
    for j in range(0, n) :
        tmp += abs(i-j)*A[j]
    if answer > tmp :
        answer = tmp

print(answer)   

