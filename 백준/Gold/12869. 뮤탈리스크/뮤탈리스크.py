import sys
from itertools import product
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
while len(array) < 3:
    array.append(0)

damage_P = [
    (9,3,1),(9,1,3),
    (3,9,1),(3,1,9),
    (1,9,3),(1,3,9)
]

# DP: dp[a][b][c] = 최소 턴 수
a0, b0, c0 = sorted(array, reverse=True)

INF = float('inf')
dp = [[[INF] * (c0+1) for _ in range(b0+1)] for _ in range(a0+1)]
dp[a0][b0][c0] = 0

# 값이 감소하는 방향이므로 현재 상태에서 줄어드는 방향으로만 탐색
from heapq import *
heap = [(0, a0, b0, c0)]

while heap:
    cnt, a, b, c = heappop(heap)
    
    if cnt > dp[a][b][c]:
        continue

    for d1, d2, d3 in damage_P:
        na, nb, nc = max(0, a-d1), max(0, b-d2), max(0, c-d3)
        # 정렬 후 저장
        na, nb, nc = sorted((na, nb, nc), reverse=True)
        
        if dp[na][nb][nc] > cnt + 1:
            dp[na][nb][nc] = cnt + 1
            heappush(heap, (cnt+1, na, nb, nc))

print(dp[0][0][0])