n = int(input())
numbers = list(map(int, input().split()))

even = sum(num % 2 == 0 for num in numbers)
odd = n - even
# 짝수가 먼저 시작해야함
# 짝수 = 홀수 + 홀수 / 짝수 하나는 그냥 홀수로 보내도 홀수
# 홀수 2개를 짝수 묶음 1개로 만들기
# 짝수의 수가 더 많다 -> 남는 짝수 묶음은 다른 묶음에 합치기

while odd > even:
    odd -= 2
    even += 1

if even > odd + 1:
    answer = odd * 2 + 1
elif odd == even:
    answer = even + odd
else:
    answer = even + odd

print(answer)