N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

now_pos = [-1] * 11
move_count = [0] * 11

for i in range(N) :
    if now_pos[pigeon[i]] == -1 :
        now_pos[pigeon[i]] = position[i]
    elif now_pos[pigeon[i]] != position[i] :
        move_count[pigeon[i]] += 1
        now_pos[pigeon[i]] = position[i]
print(sum(move_count))