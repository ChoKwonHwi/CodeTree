n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [0, 1, 0, -1] # S, E, N, W
dy = [-1, 0, 1, 0]
x, y = 0, 0
for t in range(n) :
    if dir[t] == 'N' :
        x, y = x+dx[2], y+(dy[2]*dist[t])
    elif dir[t] == 'W' :
        x, y = x+(dx[3]*dist[t]), y+dy[3]
    elif dir[t] == 'S' :
        x, y = x+dx[0], y+(dy[0]*dist[t])
    elif dir[t] == 'E' :
        x, y = x+(dx[1]*dist[t]), y+dy[1]
print(x, y)