x1, x2, x3, x4 = map(int, input().split())

# 안 겹치는 경우를 생각하기
# x2 < x3 or x4 < x1를 만족하면 안 겹침.
# 이 외의 경우를 확인

if x2 < x3 or x1 > x4 :
    print('nonintersecting')
else :
    print('intersecting')