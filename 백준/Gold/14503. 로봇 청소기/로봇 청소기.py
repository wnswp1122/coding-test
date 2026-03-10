import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:

    # 1. 현재 칸 청소
    if board[r][c] == 0:
        board[r][c] = 2
        count += 1

    moved = False

    # 2. 왼쪽 방향부터 탐색
    for _ in range(4):
        d = (d - 1) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            r = nx
            c = ny
            moved = True
            break

    if moved:
        continue

    # 3. 네 방향 모두 청소 불가 → 후진
    back = (d + 2) % 4
    nx = r + dx[back]
    ny = c + dy[back]

    # 뒤가 벽이면 종료
    if board[nx][ny] == 1:
        print(count)
        break

    # 뒤로 이동
    r = nx
    c = ny