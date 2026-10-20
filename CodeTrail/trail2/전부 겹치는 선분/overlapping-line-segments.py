n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# 좌표 list로 해당 좌표에 몇 개의 선분이 겹치는지 count하기
# 모든 선분을 각자 비교하기.
count = [0] * 101
for x, y in segments :
    for i in range(x, y+1) :
        count[i] += 1
if n in count :
    print('Yes')
else :
    print('No')