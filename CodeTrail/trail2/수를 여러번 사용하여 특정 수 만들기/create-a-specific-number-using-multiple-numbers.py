A, B, C = map(int, input().split())

bc = C//B
ac = C//A
answer = 0
for i in range(bc, -1, -1) :
    for j in range(ac, -1, -1) :
        tmp = A*j + B*i
        if tmp <= C :
            answer = max(answer, tmp)
print(answer)