n = int(input())

def up_print(i, n) :
    if i == n :
        print(i)
        return
    print(i, end=' ')
    up_print(i+1, n)

def down_print(i, n) :
    if i == 1:
        print(i)
        return
    print(i, end=' ')
    down_print(i-1, n)

up_print(1, n)
down_print(n, n)