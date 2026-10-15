X, Y = map(int, input().split())

answer = 0

for number in range(X, Y+1) :
    if len(set(list(str(number)))) != 2:
        continue
    a, b = 0, 0
    for i in str(number) :
        if list(set(str(number)))[0] == i :
            a += 1
        else :
            b += 1
    if a == 1 or b == 1 :
        answer += 1
print(answer)