n = int(input())
arr = [int(input()) for _ in range(n)]

def cal_carry(x, y, z):
    total = x + y + z

    while x or y or z:
        if x % 10 + y % 10 + z % 10 >= 10:
            return -1

        x //= 10
        y //= 10
        z //= 10

    return total
result = -1

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            result = max(result, cal_carry(arr[i], arr[j], arr[k]))
print(result)
