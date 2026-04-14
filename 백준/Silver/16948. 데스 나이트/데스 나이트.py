import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

visited = [[-1] * N for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((r1, c1))
    visited[r1][c1] = 0

    while queue:
        x, y = queue.popleft()

        if x == r2 and y == c2:
            return visited[x][y]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return -1

print(bfs())