import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

info = {} #B R C 위치 저장

# 1.R B의 위치정보 저장
for r in range(N):
    for c in range(M):
        if board[r][c] == "B":
            info['B'] = [r,c]
        if board[r][c] == "R":
            info['R'] = [r,c]
        if board[r][c] == "O":
            info['O'] = [r,c]

# 2.move 구현(움직이는 방향쪽에 있는 구슬먼저 move)
def left_tilt(info):
    if info['B'][1] < info['R'][1]:#blue가 왼쪽
        r,c = info['B']
        for i in range(c,-1,-1):
            if board[r][i] == "#":
                board[r][c] = "."
                board[r][i+1] = 'B'
                info['B'] = [r, i+1]
                break
            if r == info['O'][0] and i == info['O'][1]:
                return "Blue Goal"
        r,c = info['R']
        for i in range(c,-1,-1):
            if board[r][i] == "#" or board[r][i] == "B":
                board[r][c] = "."
                board[r][i+1] = 'R'
                info['R'] = [r, i+1]
                break
            if r == info['O'][0] and i == info['O'][1]:
                return "Red Goal"
                
    else:

        
# 3.dfs/bfs구현 dfs -> 시간복잡도? / bfs 테이블