n = int(input())
sequence = list(map(int, input().split()))

# 1개 있는 경우 생각하기
# 결국 1의 위치가 제일 중요한거 아닌가?
# 1의 위치 + 끝의 숫자만 알면 된다? N-1-(1의 index)?
# 그러기엔 이미 정렬되어있으면 0인데?
# 정렬이 아니라 그냥 끝에서부터 오름차순의 개수만 생각하면 되겠는데?

endpoint = n-1

for i in range(n-2, -1, -1) :
    if sequence[i+1] - sequence[i] > 0 :
        endpoint = i
    else :
        break
print(endpoint)