n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def f(idx):
    if idx == n - 1:
        return arr[idx]

    return lcm(f(idx + 1), arr[idx])

print(f(0))