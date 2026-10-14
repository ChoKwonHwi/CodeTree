import math

abilities = list(map(int, input().split()))

all_sum = sum(abilities)
answer = math.inf
for i in range(len(abilities)-2) :
    for j in range(i+1, len(abilities)-1) :
        for k in range(j+1, len(abilities)) :
            team1 = abilities[i] + abilities[j] + abilities[k]
            team2 = all_sum-team1
            answer = min(answer, abs(team1 - team2))
print(answer)