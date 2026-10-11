N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0 
dir_num = 0  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
cnt = 0

for i in range(N) :
    move_dir = mapper[dir[i]]
    for j in range(0, dist[i]) :
        x, y = x+dxs[move_dir], y+dys[move_dir]
        cnt += 1
        if x == 0 and y == 0 :
            print(cnt)
            exit()

print(-1)

