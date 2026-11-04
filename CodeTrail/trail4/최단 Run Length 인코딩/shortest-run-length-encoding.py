A = input()
answer = 21
if len(A) == 1 :
    print(2)
    exit()
for i in range(len(A)-1, 0, -1) :
    sen =  A[i:] + A[:i]
    bf_chr = sen[0]
    cnt = 1
    tmp_result = ""
    for idx in range(1, len(sen)) :
        if bf_chr == sen[idx] :
            cnt += 1         
        else :
            tmp_result = tmp_result + bf_chr + str(cnt)
            bf_chr = sen[idx]
            cnt = 1
    tmp_result = tmp_result + bf_chr + str(cnt)
    answer = min(answer, len(tmp_result))        
print(answer)