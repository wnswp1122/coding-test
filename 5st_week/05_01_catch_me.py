from collections import deque

def catch_me(cony_loc, brown_loc):
    MAX = 200000
    visited = [[False] * (MAX + 1) for _ in range(2)]
    queue = deque()
    queue.append(brown_loc)
    visited[0][brown_loc] = True
    time = 0
    
    while cony_loc <= MAX:
        cony = cony_loc + (time * (time + 1)) // 2
        if cony > MAX:
            return -1
        
        if visited[time % 2][cony]:
            return time
        
        for _ in range(len(queue)):
            curr = queue.popleft()
            for nxt in (curr -1, curr + 1, curr * 2):
                if 0 <= nxt <= MAX and not visited[(time + 1) % 2][nxt]:
                    visited[(time + 1) % 2][nxt] = True
                    queue.append(nxt)
        
        time += 1

print(catch_me(11, 2))  # 5
print(catch_me(10, 3))  # 3
print(catch_me(51, 50)) # 8
print(catch_me(550, 500)) # 28
