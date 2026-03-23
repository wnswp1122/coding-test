import sys
input = sys.stdin.readline

def cycle(color, x, y, cnt, start_x, start_y):
    global answer

    if answer:
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:

            if cnt >= 4 and nx == start_x and ny == start_y:
                answer = True
                return
            
            if board[ny][nx] == color and not visited[ny][nx]:
                visited[ny][nx] = True
                cycle(color, nx, ny, cnt + 1, start_x, start_y)
                visited[ny][nx] = False


def game_start():
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            cycle(board[i][j], j, i, 1, j, i)
            visited[i][j] = False

            if answer:
                return 'Yes'
    return 'No'


N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

answer = False

print(game_start())