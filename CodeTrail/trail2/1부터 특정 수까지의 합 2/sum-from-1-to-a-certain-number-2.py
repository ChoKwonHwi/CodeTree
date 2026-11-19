N = int(input())

def add_n(n) :
    if n == 1 :
        return 1
    return add_n(n-1) + n


print(add_n(N))