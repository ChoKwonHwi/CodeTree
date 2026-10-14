n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

arr = ['0']*(max(pos)+1)

for i, j in zip(pos, alpha) :
    arr[i] = j
answer = 0
result = 0

for i in range(len(arr)) :
    g_count, h_count = 0, 0
    if arr[i] == '0' :
        continue
    elif arr[i] == 'G' :
        g_count += 1
    elif arr[i] == 'H' :
        h_count += 1
    for j in range(i+1, len(arr)) :
        if arr[j] == '0' :
            continue
        if arr[j] == 'G' :
            g_count += 1
            if h_count == g_count or h_count == 0 :
                answer = max(answer, g_count+h_count)
                result = max(result, j-i)
        if arr[j] == 'H' :
            h_count += 1
            if h_count == g_count or g_count == 0 :
                answer = max(answer, h_count+g_count)
                result = max(result, j-i)
print(result)



