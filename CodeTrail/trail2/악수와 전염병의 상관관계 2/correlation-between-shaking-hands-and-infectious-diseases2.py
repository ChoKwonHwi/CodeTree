N, K, P, T = map(int, input().split())
handshakes = [list(map(int, input().split())) for _ in range(T)]

handshakes.sort(key=lambda x: x[0])

count = [-1]*(N+1)
count[P] = K

for t in range(T) :
    # a가 비감염자 -> b가 감염자
    if count[handshakes[t][1]] == -1 and count[handshakes[t][2]] > 0 :
        count[handshakes[t][1]] = K
        count[handshakes[t][2]] -= 1
    # a가 감염자 -> b가 비감염자
    elif count[handshakes[t][2]] == -1 and count[handshakes[t][1]] > 0 :
        count[handshakes[t][2]] = K
        count[handshakes[t][1]] -= 1
    # a가 감염자 -> b가 감염자    
    elif count[handshakes[t][1]] >= 0 and count[handshakes[t][2]] >= 0 :
        if count[handshakes[t][1]] == 0 and count[handshakes[t][2]] > 0 :
            count[handshakes[t][2]] -= 1
        elif count[handshakes[t][1]] > 0 and count[handshakes[t][2]] == 0 :
            count[handshakes[t][1]] -= 1
        elif count[handshakes[t][1]] > 0 and count[handshakes[t][2]] > 0 :
            count[handshakes[t][1]] -= 1
            count[handshakes[t][2]] -= 1
result = []
for i in count[1:] :
    if i != -1 :
        result.append(1)
    elif i == -1 :
        result.append(0)
print(''.join(map(str, result)))