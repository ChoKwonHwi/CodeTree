a, b = map(int, input().split())
c, d = map(int, input().split())

# 겹치면 a, c중 min ~ b, d중 max 세기
# 아니면 각자 더하기
 
if c > b or d < a :
    print(b-a + d-c)
else :
    print(max(b, d) - min(a, c))

