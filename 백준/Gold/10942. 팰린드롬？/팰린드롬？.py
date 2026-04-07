import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = 1

for i in range(1, N):
    dp[i][i+1] = 1 if arr[i] == arr[i+1] else 0

for length in range(3, N+1):
    for i in range(1, N-length+2):
        j = i + length - 1
        dp[i][j] = 1 if arr[i] == arr[j] and dp[i+1][j-1] else 0

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])