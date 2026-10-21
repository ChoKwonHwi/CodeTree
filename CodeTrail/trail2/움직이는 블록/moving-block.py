n = int(input())
blocks = [int(input()) for _ in range(n)]

m = sum(blocks)//n
answer = 0
for block in blocks :
    if block > m :
        answer += (block-m)
print(answer)