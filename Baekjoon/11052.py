import sys
import heapq
input = sys.stdin.readline

N = input()
P = list(map(int, input().split()))
pq = []
for i in range(len(P)):
    heapq.heappush(pq, -(P[i]/(i + 1)))

print(-heapq.heappop(pq))
