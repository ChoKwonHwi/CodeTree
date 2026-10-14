n = int(input())
a, b, c = [], [], []

for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)
    
ans_list = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and i != k and j != k:
                ans_list.append(100 * i + 10 * j + k)

for b_num, strike, ball in zip(a, b, c):
    b_h = b_num // 100
    b_t = b_num // 10 % 10
    b_o = b_num % 10

    next_list = []

    for num in ans_list:
        i = num // 100
        j = num // 10 % 10
        k = num % 10

        st, ba = 0, 0

        if b_h == i:
            st += 1
        if b_t == j:
            st += 1
        if b_o == k:
            st += 1

        if b_h == j or b_h == k:
            ba += 1
        if b_t == i or b_t == k:
            ba += 1
        if b_o == i or b_o == j:
            ba += 1

        if st == strike and ba == ball:
            next_list.append(num)

    ans_list = next_list

print(len(ans_list))