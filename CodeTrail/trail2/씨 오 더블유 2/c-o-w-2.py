n = int(input())
S = input()

answer = 0

for i in range(0, n-2) :
    if S[i] == 'C' :
        for j in range(i+1, n-1) :
            if S[j] == 'O' :
                for k in range(j+1, n) :
                    if S[k] == 'W' :
                        answer += 1
print(answer)