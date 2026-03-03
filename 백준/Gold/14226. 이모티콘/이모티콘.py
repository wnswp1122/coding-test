from collections import deque

MAX = 1001
S = int(input())

visited = [[False] * MAX for _ in range(MAX)]
queue = deque()

# (screen, clipboard, time)
queue.append((1, 0, 0))
visited[1][0] = True

while queue:
    screen, clipboard, time = queue.popleft()

    if screen == S:
        print(time)
        break

    # 1. 복사
    if not visited[screen][screen]:
        visited[screen][screen] = True
        queue.append((screen, screen, time + 1))

    # 2. 붙여넣기
    if clipboard > 0 and screen + clipboard < MAX:
        if not visited[screen + clipboard][clipboard]:
            visited[screen + clipboard][clipboard] = True
            queue.append((screen + clipboard, clipboard, time + 1))

    # 3. 삭제
    if screen > 0:
        if not visited[screen - 1][clipboard]:
            visited[screen - 1][clipboard] = True
            queue.append((screen - 1, clipboard, time + 1))
