inp = [list(map(int, str(input()))) for _ in range(3)]

cnt = set()

for i in range(3) :
    if (inp[0][i] == inp[1][i] and inp[0][i] != inp[2][i]) or (inp[1][i] == inp[2][i] and inp[0][i] != inp[2][i]) or (inp[0][i] == inp[2][i] and inp[0][i] != inp[1][i]):
        cnt.add(frozenset(set([inp[0][i], inp[1][i], inp[2][i]])))
    if (inp[i][0] == inp[i][1] and inp[i][1] != inp[i][2]) or (inp[i][0] == inp[i][2] and inp[i][1] != inp[i][2]) or (inp[i][1] == inp[i][2] and inp[i][1] != inp[i][0]) :
        cnt.add(frozenset(set([inp[i][0], inp[i][1], inp[i][2]])))
if (inp[0][0] == inp[1][1] and inp[0][0] != inp[2][2]) or (inp[0][0] == inp[2][2] and inp[0][0] != inp[1][1]) or (inp[2][2] == inp[1][1] and inp[0][0] != inp[2][2]) :
    cnt.add(frozenset(set([inp[0][0], inp[1][1], inp[2][2]])))
if (inp[2][0] == inp[1][1] and inp[1][1] != inp[0][2]) or (inp[0][2] == inp[1][1] and inp[2][0] != inp[0][2]) or (inp[2][0] == inp[0][2] and inp[1][1] != inp[0][2]) :
    cnt.add(frozenset(set([inp[0][2], inp[1][1], inp[2][0]])))

print(len(cnt))