board = [list(input()) for _ in range(10)]

B = [0, 0]
L = [0, 0]
R = [0, 0]
for i in range(10) :
    for j in range(10) :
        if board[i][j] == 'B' :
            B[0] = i
            B[1] = j
        elif board[i][j] == 'L' :
            L[0] = i
            L[1] = j
        elif board[i][j] == 'R' :
            R[0] = i
            R[1] = j
if (B[0] == L[0] == R[0] or B[1] == R[1] == L[1]) and ((B[0] < R[0] < L[0] or B[0] > R[0] > L[0]) or (B[1] < R[1] < L[1] or B[1] > R[1] > L[1])) :
    print(abs(L[0]-B[0]) + abs(L[1]-B[1]) + 1)
else :
    
    print(abs(L[0]-B[0]) + abs(L[1]-B[1]) - 1)
