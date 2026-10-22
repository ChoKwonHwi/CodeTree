n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

front_start = sorted(segments, key=lambda x: x[0])[1:][0][0]
tmp = sorted(segments, key=lambda x: x[0])[1:]
front_end = sorted(tmp, key=lambda x: x[1])[-1][1]

tmp = sorted(segments, key=lambda x: x[1])[:n-1]
end_start = sorted(tmp, key=lambda x: x[0])[0][0]

end_end = sorted(segments, key=lambda x: x[1])[:n-1][-1][1]

print(min(front_end-front_start, end_end-end_start))