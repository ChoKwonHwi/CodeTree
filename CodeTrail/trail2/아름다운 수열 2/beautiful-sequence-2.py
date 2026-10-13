N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))

result = 0

for i in range(N-M+1) :
    if sorted(A[i:i + M]) == B:
        result += 1
print(result)