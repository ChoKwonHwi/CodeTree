n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

while True:
    remaining = []
    exploded = False
    i = 0

    while i < len(numbers):
        # i부터 같은 숫자가 어디까지 이어지는지 찾기
        j = i + 1

        while j < len(numbers) and numbers[j] == numbers[i]:
            j += 1

        # 같은 숫자의 구간: numbers[i:j]
        count = j - i

        if count >= m:
            exploded = True
        else:
            remaining.extend(numbers[i:j])

        i = j

    numbers = remaining

    if not exploded:
        break

print(len(numbers))
for num in numbers:
    print(num)