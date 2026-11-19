n = int(input())

def hello(i, n) :
    if i == n :
        return
    else :
        print('HelloWorld')
        hello(i+1, n)
hello(0, n)