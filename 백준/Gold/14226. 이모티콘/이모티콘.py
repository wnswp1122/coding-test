from collections import deque
import sys

input = sys.stdin.readline

S = int(input())
MAX = 1001  

visited = [[False] * MAX for _ in range(MAX)]

queue = deque()
queue.append((1, 0, 0)) 
visited[1][0] = True

while queue:
    screen, clip, time = queue.popleft()

    if screen == S:
        print(time)
        break

    if not visited[screen][screen]:
        visited[screen][screen] = True
        queue.append((screen, screen, time + 1))

    if clip > 0 and screen + clip < MAX and not visited[screen + clip][clip]:
        visited[screen + clip][clip] = True
        queue.append((screen + clip, clip, time + 1))

    if screen > 0 and not visited[screen - 1][clip]:
        visited[screen - 1][clip] = True
        queue.append((screen - 1, clip, time + 1))