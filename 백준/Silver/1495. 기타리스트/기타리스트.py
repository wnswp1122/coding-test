import sys
input = sys.stdin.readline

N, S, K = map(int, input().split())
volume = list(map(int, input().split()))

dp = [set() for _ in range(N + 1)]
dp[0].add(S)

for i in range(1, N + 1):
    v = volume[i - 1]
    for cur in dp[i - 1]:
        if 0 <= cur + v <= K:
            dp[i].add(cur + v)
        if 0 <= cur - v <= K:
            dp[i].add(cur - v)

if not dp[N]:
    print(-1)
else:
    print(max(dp[N]))