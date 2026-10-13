n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    for j in range(n - 2):
        cnt1 = sum(arr[i][j:j + 3])

        for k in range(n):
            for l in range(n - 2):
                # 같은 행에서 가로 구간이 겹치면 제외
                if i == k and abs(j - l) < 3:
                    continue

                cnt2 = sum(arr[k][l:l + 3])
                result = max(result, cnt1 + cnt2)

print(result)