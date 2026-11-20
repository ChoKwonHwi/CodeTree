n = int(input())

def f(n, cnt) :
    if n == 1 :
        return cnt
    if n%2 == 0 :
        return f(n//2, cnt+1)
    elif n%2 == 1 :
        return f(3*n+1, cnt+1)
print(f(n, 0))