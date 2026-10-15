X, Y = map(int, input().split())

answer = 0

for number in range(X, Y+1) :
    tmp_number = number
    tmp = 0
    while tmp_number > 0 :
        tmp += tmp_number%10
        tmp_number //= 10
    answer = max(answer, tmp)
print(answer)