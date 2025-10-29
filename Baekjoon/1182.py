N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(1, 1 << N):  # 1부터 시작: 공집합 제외
    total = 0
    for j in range(N):
        if i & (1 << j):
            total += arr[j]
    if total == S:
        count += 1

print(count)
