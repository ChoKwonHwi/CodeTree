import math
X = int(input())

# 최선은 세모 형태 t * t  <= X 인 최대 t 찾기 
# X = t² → 2t-1초
# t² < X ≤ t²+t → 2t초
# t²+t < X < (t+1)² → 2t+1초

t = math.isqrt(X)

if X == t**2 :
    print(2 * t - 1)
elif t**2 < X <= t**2 + t :
    print(2 * t)
elif t**2 + t < X < (t+1)**2 :
    print(2 * t + 1)