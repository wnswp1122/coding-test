import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for x in range(N):
    for y in range(M):
        if matrix[x][y] == 1:
            queue.append((x, y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

# 결과 계산
result = 0
for row in matrix:
    for value in row:
        if value == 0:
            print(-1)
            exit()
        result = max(result, value)

print(result - 1)