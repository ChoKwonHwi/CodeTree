N = int(input())

def f(t, n) :
    if t <= 0 :
        return
    print(t, end=' ')
    f(t-1, n)
    print(t, end=' ')    


f(N, N)

