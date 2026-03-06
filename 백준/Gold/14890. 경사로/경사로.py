import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(path):
    used = [False] * N

    for i in range(1, N):
        diff = path[i] - path[i-1]

        if diff == 0:
            continue

        elif diff == 1:  # 올라가는 경사
            for j in range(i-L, i):
                if j < 0 or path[j] != path[i-1] or used[j]:
                    return False
                used[j] = True

        elif diff == -1:  # 내려가는 경사
            for j in range(i, i+L):
                if j >= N or path[j] != path[i] or used[j]:
                    return False
                used[j] = True

        else:
            return False

    return True

answer = 0

# 행 검사
for row in board:
    if check(row):
        answer += 1

# 열 검사
for col in zip(*board):
    if check(col):
        answer += 1

print(answer)