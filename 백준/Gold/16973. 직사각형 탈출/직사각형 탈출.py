from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
h, w, sr, sc, fr, fc = map(int, input().split())
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
psum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+a[i-1][j-1]
q = deque([(sr-1, sc-1)])
visited[sr-1][sc-1] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    if x == fr-1 and y == fc-1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        x1, y1 = nx+1, ny+1
        x2, y2 = x1+h-1, y1+w-1
        if (0 <= nx and 0 <= ny) and (nx+h <= n and ny+w <= m) and not (psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1]) > 0:
            if not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
print(visited[fr-1][fc-1] - 1)