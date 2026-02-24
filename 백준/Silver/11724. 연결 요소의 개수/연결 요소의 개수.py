import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [ [0] * N for _ in range(N)]

for i in range(M):
    u,v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

visited = [False] * N

def count_node():
    count = 0
    for i in range(N):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

def dfs(v):
    visited[v] = True
    for i in range(N):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)

print(count_node())