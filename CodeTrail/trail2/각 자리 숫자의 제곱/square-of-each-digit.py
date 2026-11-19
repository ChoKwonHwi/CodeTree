N = int(input())

def f(N) :  
    if N == 0 :
        return 0
    return f(N//10) + (N%10)**2
print(f(N))