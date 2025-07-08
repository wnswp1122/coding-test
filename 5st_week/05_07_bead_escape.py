import sys
from collections import deque
input = sys.stdin.readline

board = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
N, M = len(board), len(board[0])

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def move(r, c, dr, dc):
    move_count = 0
    while not(board[r][c] == "O" or board[r + dr][c + dc] == "#"):
        r += dr
        c += dc
        move_count += 1
    return r, c, move_count
 
def bfs():
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)] #visited[][][][]
    queue = deque()
    for r in range(N):
        for c in range(M):
            if board[r][c] == "B":
                blue_r, blue_c = r, c
            elif board[r][c] == "R":
                red_r, red_c = r, c
    queue.append((blue_r,blue_c,red_r,red_c, 1))
    visited[blue_r][blue_c][red_r][red_c] = True

    while queue:
        blue_r, blue_c, red_r, red_c, try_count = queue.popleft()
        if try_count > 10:
            break
        
        for i in range(4):
            next_blue_r, next_blue_c, b_count = move(blue_r, blue_c, dr[i], dc[i])
            next_red_r, next_red_c, r_count = move(red_r, red_c, dr[i], dc[i])

            if board[next_blue_r][next_blue_c] == "O":
                continue
            if board[next_red_r][next_red_c] == "O":
                return True
            
            if next_blue_r == next_red_r and next_blue_c == next_red_c:
                if b_count > r_count:
                    next_red_r -= dr[i]
                    next_red_c -= dc[i]
                else:
                    next_blue_r -= dr[i]
                    next_blue_c -= dc[i]

            if not visited[next_blue_r][next_blue_c][next_red_r][next_red_c]:
                visited[next_blue_r][next_blue_c][next_red_r][next_red_c] = True
                queue.append((next_blue_r,next_blue_c,next_red_r,next_red_c, try_count + 1))
    
    return False

print("정답 = False / 현재 풀이 값 = ", bfs())