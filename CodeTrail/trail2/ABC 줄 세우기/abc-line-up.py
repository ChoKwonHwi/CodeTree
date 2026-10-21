n = int(input())
arr = list(input().split())

# 역순으로 가는게 맞을까?
# D부터 하는데, 4-D(현재위치)만큼 처음에 움직일거임.
# 다음 C는 3-C(현재위치)
# 다음 B는 2-B(현재위치), A는 자연스럽게 맞춰짐.

answer = 0

for target in range(n - 1, 0, -1):
    ch = chr(ord('A') + target)
    pos = arr.index(ch)

    while pos < target:
        arr[pos], arr[pos + 1] = arr[pos + 1], arr[pos]
        pos += 1
        answer += 1

print(answer)
