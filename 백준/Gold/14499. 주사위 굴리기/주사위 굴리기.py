import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0]*6

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def roll(dir):
    global dice
    top, bottom, north, south, west, east = dice

    if dir == 1:  # 동
        dice = [west, east, north, south, bottom, top]
    elif dir == 2:  # 서
        dice = [east, west, north, south, top, bottom]
    elif dir == 3:  # 북
        dice = [south, north, top, bottom, west, east]
    elif dir == 4:  # 남
        dice = [north, south, bottom, top, west, east]

for c in commands:
    nx = x + dx[c-1]
    ny = y + dy[c-1]

    if not (0 <= nx < N and 0 <= ny < M):
        continue

    roll(c)
    x, y = nx, ny

    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0

    print(dice[0])