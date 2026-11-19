N = int(input())

def f(N) :
    if N == 1 :
        return 0
    if N%2 == 1 :
        return f(N//3) + 1
    else :
        return f(N//2) + 1

print(f(N))