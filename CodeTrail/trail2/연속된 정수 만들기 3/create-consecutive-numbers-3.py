a = list(map(int, input().split()))

# x, y, z라고 하면, x와 y사이의 거리 & y와 z 사이의 거리 중 큰 값 -1 아닌가?
a = sorted(a)
print(max(a[2]-a[1], a[1]-a[0])-1)