N = int(input())
str = input()

# 1부터 확인 -> 겹치면 continue

for i in range(1, N) : # 문자열 길이
    li = []
    for j in range(N-i+1) :
        li.append(str[j:j+i])
    if len(li) == len(set(li)) :
        print(i)
        break
    
        
