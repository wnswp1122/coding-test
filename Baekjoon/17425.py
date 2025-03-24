dp = [0] * 1000001 # 약수의 합을 저장할 list

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        dp[j] += i # 배수들에 i를 더해줌 (i를 약수로 가지므로)
    dp[i] += dp[i - 1] # 이전단계까지 구한 합을 더해 누적 합 계산

for tc in range(int(input())): # 테스트 케이스 개수만큼 반복
    n = int(input()) # 자연수 n
    print(dp[n])    

#python으로 하면 시간초과 (pypy3 사용)