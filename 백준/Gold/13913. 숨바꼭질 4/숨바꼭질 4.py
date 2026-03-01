from collections import deque
import sys

MAX = 100001
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [False] * MAX
parents = [-1] * MAX

queue = deque([(N, 0)])
visited[N] = True

while queue:
    X, count = queue.popleft()

    if X == K:
        print(count)

        path = []
        cur = K
        while cur != -1:
            path.append(cur)
            cur = parents[cur]

        path.reverse()
        print(*path)
        break

    for nx in (X-1, X+1, 2*X):
        if 0 <= nx < MAX and not visited[nx]:
            visited[nx] = True
            parents[nx] = X
            queue.append((nx, count+1))