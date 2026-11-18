import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dirs = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

T = int(input())
answers = []

for _ in range(T):
    N, M = map(int, input().split())
    size = N * N

    marbles = []
    for _ in range(M):
        x, y, d = input().split()
        pos = (int(x) - 1) * N + int(y) - 1
        marbles.append(pos * 4 + dirs[d])

    next_state = [0] * (size * 4)

    for x in range(N):
        for y in range(N):
            pos = x * N + y

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < N:
                    nxt = (nx * N + ny) * 4 + d
                else:
                    nxt = pos * 4 + (d + 2) % 4

                next_state[pos * 4 + d] = nxt

    for _ in range(2 * N):
        if len(marbles) <= 1:
            break

        moved = [next_state[s] for s in marbles]
        counts = [0] * size

        for s in moved:
            counts[s >> 2] += 1

        marbles = [s for s in moved if counts[s >> 2] == 1]

    answers.append(str(len(marbles)))

print('\n'.join(answers))