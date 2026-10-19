nums = list(map(int, input().split()))


def is_equal_array(arr1, arr2):
    arr1.sort()
    arr2.sort()

    if len(arr1) != len(arr2):
        return False

    for x, y in zip(arr1, arr2):
        if x != y:
            return False

    return True

maximum = max(nums)-3

for a in range(1, maximum+1):
    for b in range(a, maximum+1):
        for c in range(b, maximum+1):
            for d in range(c, maximum+1) :
                if is_equal_array([a, b, c, d, a+b, a+c, a+d, b+c, b+d, c+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d], nums):
                    print(a, b, c, d)

