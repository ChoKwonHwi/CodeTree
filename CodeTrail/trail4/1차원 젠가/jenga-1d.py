n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

s1, s2 = s1-1, s2-1

del blocks[s1:e1]
del blocks[s2:e2]
if len(blocks) == 0 :
    print(0)
else :
    print(len(blocks))
    for block in blocks :
        print(block)