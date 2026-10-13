A = input()

cnt = 0

for i in range(0, len(A)) :
    if A[i] == ')' :
        continue
    for j in range(i, len(A)) :
        if A[j] == ')' :
            cnt+=1
print(cnt) 