import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
max_money = [0] * (N + 1)  # ✅ 리스트 크기 충분히 확보

for i in range(N):
    t, p = map(int, input().split(" "))
    T.append(t)
    P.append(p)

for i in range(N - 1, -1, -1):
    if i + T[i] > N:
        max_money[i] = max_money[i + 1]
    else:
        max_money[i] = max(max_money[i + 1], P[i] + max_money[i + T[i]])

print(max_money[0])
