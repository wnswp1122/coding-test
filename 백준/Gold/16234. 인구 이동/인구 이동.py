import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    union = [(x, y)]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(grid[cx][cy] - grid[nx][ny])
                if l <= diff <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union

days = 0
while True:
    visited = [[False]*n for _ in range(n)]
    moved = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs(i, j, visited)
                if len(union) > 1:
                    moved = True
                    avg = sum(grid[x][y] for x, y in union) // len(union)
                    for x, y in union:
                        grid[x][y] = avg
    if not moved:
        break
    days += 1

print(days)