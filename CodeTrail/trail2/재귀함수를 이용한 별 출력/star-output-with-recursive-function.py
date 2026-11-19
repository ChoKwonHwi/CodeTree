n = int(input())

def star(i, n) :
    if i == n :
        print('*'*n)
        return
    print('*'*i)
    star(i+1, n)

star(1, n)