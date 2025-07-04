import sys
input = sys.stdin.readline

N, M = map(int, input().split())
town_map = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []

# 치킨집과 집 위치 분리 저장
for r in range(N):
    for c in range(N):
        if town_map[r][c] == 2:
            chicken.append((r, c))
        elif town_map[r][c] == 1:
            house.append((r, c))

# distance[i][j] = i번 치킨집과 j번 집의 거리
distance = [[] for _ in range(len(chicken))]

for i, (cr, cc) in enumerate(chicken):
    for hr, hc in house:
        dist = abs(cr - hr) + abs(cc - hc)
        distance[i].append(dist)

min_result = float('inf')
stack = []

def dfs(start):
    global min_result

    if len(stack) == M:
        min_arr = [float('inf')] * len(house)
        for s in stack:
            for i in range(len(house)):
                min_arr[i] = min(min_arr[i], distance[s][i])
        min_result = min(min_result, sum(min_arr))
        return

    for i in range(start, len(chicken)):
        stack.append(i)
        dfs(i + 1)
        stack.pop()

dfs(0)
print(min_result)
