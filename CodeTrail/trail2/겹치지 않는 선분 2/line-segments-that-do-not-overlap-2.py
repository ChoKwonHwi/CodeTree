n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

#lines[i][0], lines[i][1], lines[j][0], lines[j][1]

# 겹치지 않는다 -> 

answer = [0] * n

for i in range(n):
    for j in range(i+1, n) :
        if not((lines[i][0] < lines[j][0] and lines[i][1] < lines[j][1]) or (lines[i][0] > lines[j][0] and lines[i][1] > lines[j][1])) :
            answer[i] = 1
            answer[j] = 1
print(answer.count(0))