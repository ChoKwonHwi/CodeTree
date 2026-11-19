n = int(input())

def f(t, n) :
    if t <= 0 :
        return
    print('* '*t)
    f(t-1, n)
    print('* '*t)

f(n, n)