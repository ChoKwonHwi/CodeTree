a, b, c = map(int, input().split())

# 0 : 시작부터 연속되게 있는 경우
# 1 : a, b / b, c의 차이가 2인 경우
# 2 : 
if max(a, b, c) - min(a, b, c) == 2:
    print(0) 
elif abs(a-b) == 2 or abs(b-c) == 2 :
    print(1)
else :
    print(2)