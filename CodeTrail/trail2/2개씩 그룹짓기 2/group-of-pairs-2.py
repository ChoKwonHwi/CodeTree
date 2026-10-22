n = int(input())
arr = list(map(int, input().split()))

# 1 2 3 5 6 50 39 80 -> 1 2 3 5 6 39 50 80 -> 1 6
# 정렬 후 N개 N개 나누고 묶어보면 될듯

arr = sorted(arr)
front, end = arr[:n], arr[n:]
answer = []

for i in range(n) :
    answer.append(end[i]-front[i])
print(min(answer))