n = int(input())
lr = list(list(map(int, input().split())) for _ in range(n))

answer = 0

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            line = [0] * 101
            for l in range(n) :
                if l == i or l == j or l == k :
                    continue
                else :
                    for m in range(lr[l][0], lr[l][1]+1) :
                        line[m] += 1
            if not any(ss >= 2 for ss in line):
                answer += 1
print(answer)