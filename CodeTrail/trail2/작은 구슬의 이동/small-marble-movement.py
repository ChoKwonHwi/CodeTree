n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

move_dir = mapper[d]

x, y = r-1, c-1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for times in range(t) :
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):
        if move_dir == 1 :
            move_dir = mapper['U']
        elif move_dir == 2 :
            move_dir = mapper['D']
        elif move_dir == 3 :
            move_dir = mapper['R']
        elif move_dir == 0 :
            move_dir = mapper['L']
        continue

    x, y = x + dxs[move_dir], y + dys[move_dir]

print(x+1, y+1)