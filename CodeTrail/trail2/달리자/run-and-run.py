n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

people = 0
cost = 0
for i in range(n-1) :
    people += A[i] - B[i]
    cost += people
print(cost)
