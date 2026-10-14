N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

arr = [0]*(max(pos)+1)

for i, j in zip(candy, pos) :
    arr[j] += i

answer = 0

for idx in range(0, len(arr)) :
    start = max(0, idx-K)
    end = min(len(arr), idx+K+1)

    selected = arr[start:end]

    answer = max(answer, sum(selected))
print(answer)