import sys
input = sys.stdin.readline

N, M = map(int, input().split())
town_map = [list(map(int, input().split())) for _ in range(N)]

chicken = []
distance = []

for r in range(N):
    for c in range(N):
        if town_map[r][c] == 2:
            chicken.append((r,c))
            distance.append([])

for r in range(N):
    for c in range(N):
        if town_map[r][c] == 1:
            for i in range(len(chicken)):
                distance[i].append(abs(chicken[i][0] - r) + abs(chicken[i][1] - c))

stack = []
min_result = float('inf')
def dfs(start):
    global min_result
    if len(stack) == M:
        min_arr = distance[stack[0]][:]
        for s in range(1,M):
            for i in range(len(distance[0])):
                if min_arr[i] > distance[stack[s]][i]:
                    min_arr[i] = distance[stack[s]][i]
        min_result = min(min_result,sum(min_arr))

    for i in range(start,len(chicken)):
        stack.append(i)
        dfs(i + 1)
        stack.pop()

    return min_result

print(dfs(0))