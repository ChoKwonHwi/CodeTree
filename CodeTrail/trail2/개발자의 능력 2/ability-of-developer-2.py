import math

ability = list(map(int, input().split()))

answer = math.inf

for i in range(0, len(ability)-1) :
    for j in range(i+1, len(ability)) :
        team1 = ability[i] + ability[j]
        tmp_ab = ability.copy()
        del tmp_ab[j]
        del tmp_ab[i]
        for k in range(len(tmp_ab)-1) :
            for l in range(k+1, len(tmp_ab)) :
                team2 = tmp_ab[k] + tmp_ab[l]
                team3 = sum(tmp_ab) - team2
                answer = min(answer, max(team1, team2, team3) - min(team1, team2, team3))
print(answer)