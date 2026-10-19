n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

counts = {}

for a, b in pairs:
    key = frozenset({a, b})
    counts[key] = counts.get(key, 0) + 1

print(max(counts.values(), default=0))  