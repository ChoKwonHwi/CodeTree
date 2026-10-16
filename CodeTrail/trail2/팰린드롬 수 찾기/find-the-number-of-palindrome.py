X, Y = map(int, input().split())
cnt = 0
for num in range(X, Y+1) :
    if list(str(num)) == list(str(num))[::-1] :
        cnt += 1
print(cnt)
