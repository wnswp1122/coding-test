import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
degree = [0] * N

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    degree[a] += 1
    degree[b] += 1

# 1. 사이클 찾기 (leaf 제거)
queue = deque()
for i in range(N):
    if degree[i] == 1:
        queue.append(i)

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        degree[nxt] -= 1
        if degree[nxt] == 1:
            queue.append(nxt)

# degree >= 2 인 노드 = 사이클
dist = [-1] * N
queue = deque()

# 2. 사이클 노드 초기화
for i in range(N):
    if degree[i] >= 2:
        dist[i] = 0
        queue.append(i)

# 3. BFS
while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            queue.append(nxt)

print(*dist)