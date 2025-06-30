dp = [0,1,2,4,0,0,0,0,0,0,0,0,0,0,0]

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

N = int(input())
for i in range(N):
    k = int(input())
    print(dp[k])