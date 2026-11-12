N = int(input())
x, y = map(int, input().split())

grid = [["."] * N for _ in range(N)]
for i in range(0, N):
    row = input()
    for j in range(0, N):
        grid[i][j] = row[j]

x, y = x-1, y-1
# case0 : 지나간 위치는 X로 표시하고, 만일 다시 X로 돌아오면 loop에 빠진 것으로 판단하고 -1 출력 후 exit
# case1 : 바라보고 있는 방향으로 이동 불가 : 반시계 dir 바꾸기
# case2 : 바라보고 있는 방향 이동 가능 : 바로앞이 격자 밖 : 탈출(grid 바깥 범위 체크하기) -> 1초
# case3 : 바라보고 있는 방향 이동 가능 : 오른쪽에 짚을 벽이 있으면 그 방향으로 한 칸 이동 -> 1초
# case4 : 이동했는데 오른쪽 벽이 없는 경우 : dir 시계 바꾸고 한칸 더 가서 오른쪽이 있게 만들기 -> 2초
# 방향 바꾸는 것은 시간 걸리지 않고 이동하는데 1초의 시간

dir_num = 3 # 하, 좌, 상, 우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def is_range(nx, ny) :
    return 0 <= nx < N and 0 <= ny < N

answer = 0
visited = set()
while True :
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    
    if (x, y, dir_num) in visited:
        print(-1)
        exit()
    
    visited.add((x, y, dir_num))

    if not is_range(nx, ny) : # case2
        answer += 1
        print(answer)
        exit()

    if is_range(nx, ny) and grid[nx][ny] == '.' :
        answer += 1
        x, y = nx, ny

        dir_num_right = (dir_num + 1) % 4
        tx, ty = x + dx[dir_num_right], y + dy[dir_num_right]

        if is_range(tx, ty) and grid[tx][ty] == '#' :
            continue
        else :
            dir_num = dir_num_right
            answer += 1
            if not is_range(tx, ty):
                print(answer)
                exit()
            x, y = tx, ty

    elif is_range(nx, ny) and grid[nx][ny] == '#' : # case1
        dir_num = (dir_num + 3) % 4
    
    
print(answer)