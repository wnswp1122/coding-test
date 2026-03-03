from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dp = [[float('inf')] * N for _ in range(M)]
dp[0][0] = 0

queue = deque()
queue.append((0, 0))

while queue:
    y, x = queue.popleft()

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < M and 0 <= nx < N:
            cost = dp[y][x] + maze[ny][nx]

            if cost < dp[ny][nx]:
                dp[ny][nx] = cost

                if maze[ny][nx] == 0:
                    queue.appendleft((ny, nx))
                else:
                    queue.append((ny, nx))

print(dp[M-1][N-1])