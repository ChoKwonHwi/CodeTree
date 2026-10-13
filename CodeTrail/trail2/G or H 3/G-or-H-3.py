n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

result = 0
score = [0] * (max(x)+1)

for i, j in zip(x, c) :
    if j == 'H' :
        score[i] = 2
    elif j == 'G' :
        score[i] = 1

if k >= max(x):
    result = sum(score)
else:
    for i in range(len(score) - k):
        result = max(result, sum(score[i:i+k+1]))
print(result)