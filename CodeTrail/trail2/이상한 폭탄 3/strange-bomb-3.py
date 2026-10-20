N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

num_check = [False] * len(num)
bomb_list = [0]*(max(num)+1)

for i in range(N-1) :
    for j in range(i+1, N) :
        if num[i] == num[j] and abs(i-j) <= K :
            if num_check[i] == False :
                bomb_list[num[i]] += 1
                num_check[i] = True
            if num_check[j] == False :
                bomb_list[num[j]] += 1
                num_check[j] = True
           
answer, ans_idx = 0, 0
for idx, n in enumerate(bomb_list) :
    if answer <= n :
        answer = n
        ans_idx = idx
if not any(num_check):
    print(0)
else :
    print(ans_idx)