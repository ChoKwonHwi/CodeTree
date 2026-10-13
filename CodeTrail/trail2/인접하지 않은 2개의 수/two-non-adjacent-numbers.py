n = int(input())
numbers = list(map(int, input().split()))
answer = 0
for i in range(n-2) :
    for j in range(i+2, n) :
        answer = max(answer, numbers[i]+numbers[j])
print(answer)