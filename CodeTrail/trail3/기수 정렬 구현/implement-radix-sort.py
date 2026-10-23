n = int(input())
arr = list(map(int, input().split()))

for i in range(5, -1, -1):
    arr_new = list([] for _ in range(10))

    for j in range(len(arr)):
        arr[j] = str(arr[j]).zfill(6)
        arr_new[int(arr[j][i])].append(arr[j])

    store_arr = []
    for j in range(10):
        for k in range(len(arr_new[j])):
            store_arr.append(int(arr_new[j][k]))

    arr = store_arr

print(*arr)

