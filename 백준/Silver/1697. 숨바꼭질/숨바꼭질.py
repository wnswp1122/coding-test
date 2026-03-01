from collections import deque
import sys

MAX = 100001
input = sys.stdin.readline

N,K = map(int, input().split())
visited = [False] * MAX
queue = deque()
queue.append([N,0])

visited[N] = True

while True:
    X, count = queue.popleft()
    if X == K:
        print(count)
        exit()
    for nx in (X-1, X+1, 2*X):
        if 0 <= nx < MAX and not visited[nx]:
            visited[nx] = True
            queue.append((nx, count+1))

