import sys
input = sys.stdin.readline

N = int(input())
miro = list(map(int, input().split()))

INF = int(1e9)
dp = [INF] * N
dp[0] = 0  # 시작 위치

for i in range(N):
    if dp[i] == INF:
        continue  

    for j in range(1, miro[i] + 1):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[N - 1] if dp[N - 1] != INF else -1)