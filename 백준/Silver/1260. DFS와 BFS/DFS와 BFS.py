import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

g = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    g[x-1][y-1] = 1
    g[y-1][x-1] = 1


# DFS
visited = [False] * N
dfs_list = []

def dfs(v):
    visited[v] = True
    dfs_list.append(v+1)

    for i in range(N):
        if g[v][i] == 1 and not visited[i]:
            dfs(i)

dfs(V-1)
print(*dfs_list)


# BFS
visited = [False] * N
bfs_list = []

def bfs(start):
    queue = [start]
    visited[start] = True
    front = 0

    while front < len(queue):
        v = queue[front]
        front += 1

        bfs_list.append(v+1)

        for i in range(N):
            if g[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(V-1)
print(*bfs_list)
