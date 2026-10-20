n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# 과연 p번째 메세지 이후만 확인하면 되는가? -> 아니다.
# p번째 이후 기록과 대조해야한다.
# A~ 리스트를 만들고 제외하는 방식으로 가는것이 나을까?
# 이전 메시지 중 미열람 수가 같은 것과, p번째 이후 메시지를 보낸 사람 모두 제외
target = u[p - 1]

if target == 0:
    print()

else:
    read = set()

    for i in range(m):
        if u[i] >= target:
            read.add(c[i])

    people = []

    for i in range(n):
        name = chr(ord('A') + i)
        if name not in read:
            people.append(name)

    print(*people)



