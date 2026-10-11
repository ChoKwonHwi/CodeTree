commands = list(input())

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
x, y = 0, 0 

dir_num = 0
cnt = 0

for cmd in commands :
    if cmd == 'L' :
        dir_num = (dir_num + 3) % 4
    elif cmd == 'R' :
        dir_num = (dir_num + 1) % 4
    elif cmd == 'F' :
        x, y = x + dxs[dir_num], y + dys[dir_num]
    cnt += 1
    if x == 0 and y == 0 :
        print(cnt)
        exit()

print(-1)