import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = -1


def DFS(L, x, y, total):
    global answer
    if L == 4:
        answer = max(answer, total)
    elif (total+max_value*(4-L)) <= answer: # 변경점2
        return
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                if L == 2: # 변경점 1
                    DFS(L+1, x, y, total+board[xx][yy])
                DFS(L+1, xx, yy, total+board[xx][yy])
                ch[xx][yy] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ch = [[0]*M for _ in range(N)]
    max_value = max(map(max, board)) # 변경점2

    for i in range(0, N):
        for j in range(0, M):
            ch[i][j] = 1
            DFS(1, i, j, board[i][j])
            ch[i][j] = 0

    print(answer)