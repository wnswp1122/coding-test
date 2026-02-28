import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def count_knight():
    I = int(input())
    visited = [[-1] * I for _ in range(I)]
    
    queue = deque()
    start = list(map(int, input().split()))
    visited[start[0]][start[1]] = 0
    queue.append(start)

    target = list(map(int, input().split()))

    while queue:
        x, y = queue.popleft()

        if x == target[0] and y == target[1]:
            return visited[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

for _ in range(K):
    print(count_knight())