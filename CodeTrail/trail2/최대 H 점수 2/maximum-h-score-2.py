N, L = map(int, input().split())
a = list(map(int, input().split()))

# 0. 0부터 N까지 H를 정한다.
# 1. 서로 다른 L개를 1씩 올린다 -> H와 1만 차이나는 값만 생각하면 된다.
# 2. 순회하며 H과 1차이 나는 값의 개수를 구한다. -> l_count -> min(L, H-1인 원소의 수)
# 3. minus_cnt + H 이상의 수의 개수 >= H개 : answer 갱신
# H 이상인 원소 수 + min(L, H-1인 원소 수) ≥ H 를 찾기

answer = 0

for H in range(0, N+1) :
    l_count = 0
    h_up = 0
    for i in a :
        if i == H-1 :
            l_count += 1
        elif i >= H :
            h_up += 1
    
    if h_up + min(L, l_count) >= H :
        answer = max(answer, H)
print(answer)