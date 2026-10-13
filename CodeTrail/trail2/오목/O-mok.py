board = [list(map(int, input().split())) for _ in range(19)]

def in_range(x, y) :
    return 0 <= x and x < 19 and 0 <= y and y < 19

for i in range(19) :
    for j in range(19) :
        if board[i][j] != 0 :
            now = board[i][j]
            cnt = 0
            for k in range(1, 5) :
                if in_range(i+k, j) and board[i+k][j] == now :
                    cnt += 1
            if cnt == 4 :
                print(now)
                print(i+3, j+1)
                exit()

            cnt = 0
            for k in range(1, 5) :
                if in_range(i, j+k) and board[i][j+k] == now :
                    cnt += 1
            if cnt == 4 :
                print(now)
                print(i+1, j+3)
                exit()

            cnt = 0
            for k in range(1, 5) :
                if in_range(i+k, j+k) and board[i+k][j+k] == now :
                    cnt += 1
            if cnt == 4 :
                print(now)
                print(i+3, j+3)
                exit()

            cnt = 0
            for k in range(1, 5):
                if in_range(i-k, j+k) and board[i-k][j+k] == now:
                    cnt += 1

            if cnt == 4:
                print(now)
                print(i-1, j+3)
                exit()
print(0)