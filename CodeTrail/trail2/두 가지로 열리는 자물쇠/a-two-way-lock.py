N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

answer = 0

for i in range(1, N+1) :
    for j in range(1, N+1) :
        for k in range(1, N+1) :
            if (((abs(a1-i) <= 2) or (N - abs(a1-i) <= 2)) and (abs(b1-j) <= 2 or (N - abs(b1-j) <= 2)) and (abs(c1-k) <= 2 or (N - abs(c1-k) <= 2))) or (((abs(a2-i) <= 2) or (N - abs(a2-i) <= 2)) and (abs(b2-j) <= 2 or (N - abs(b2-j) <= 2)) and (abs(c2-k) <= 2 or (N - abs(c2-k) <= 2))) :
                answer +=1
print(answer)