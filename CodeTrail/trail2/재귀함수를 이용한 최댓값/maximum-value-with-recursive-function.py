n = int(input())
arr = list(map(int, input().split()))

def f(arr, n, i, m) :
    if i == n :
        return m
    if arr[i] > m :
        m = arr[i]
    return f(arr, n, i+1, m)

print(f(arr, n, 0, 0))