from collections import deque
import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

min_dim = min(N, M)

for i in range(min_dim // 2):

    top = i
    left = i
    bottom = N - 1 - i
    right = M - 1 - i

    total = 2 * ((bottom - top) + (right - left))
    rotate_cnt = R % total

    queue = deque()

    for row in range(top, bottom):
        queue.append(arr[row][left])

    for col in range(left, right):
        queue.append(arr[bottom][col])

    for row in range(bottom, top, -1):
        queue.append(arr[row][right])

    for col in range(right, left, -1):
        queue.append(arr[top][col])

    queue.rotate(rotate_cnt)

    for row in range(top, bottom):
        arr[row][left] = queue.popleft()

    for col in range(left, right):
        arr[bottom][col] = queue.popleft()

    for row in range(bottom, top, -1):
        arr[row][right] = queue.popleft()

    for col in range(right, left, -1):
        arr[top][col] = queue.popleft()

for row in arr:
    print(*row)