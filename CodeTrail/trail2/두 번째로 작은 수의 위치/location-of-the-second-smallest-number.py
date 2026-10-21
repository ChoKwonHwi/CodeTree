n = int(input())
a = list(map(int, input().split()))

b = sorted(a)
minimum = b[0]
answer = 0
ans_idx = -1
find = False
for idx, num in enumerate(b) :
    if num == minimum :
        continue
    if num != minimum and answer != num and find == False:
        find = True
        ans_idx = idx
        answer = num
    elif num != minimum and answer == num :
        print(-1)
        exit()
if find :
    for i, num in enumerate(a) :
        if num == answer :
            print(i+1)
            break
else :
    print(-1)
    

