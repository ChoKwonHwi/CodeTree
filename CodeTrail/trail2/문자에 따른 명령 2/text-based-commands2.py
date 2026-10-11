dirs = input()

commands = list(dirs)

dir_num = 3
x, y = 0, 0

# 0: 동 / 1: 서 / 2: 남 / 3: 북
dx = [1, 0, -1, 0]
dy =  [0, -1, 0, 1]

for cmd in commands :
    if cmd == 'F' :
        x, y = x + dx[dir_num], y + dy[dir_num]
    elif cmd == 'L' :
        dir_num = (dir_num + 3) % 4
    elif cmd == 'R' :
        dir_num = (dir_num + 1) % 4

print(x, y)
