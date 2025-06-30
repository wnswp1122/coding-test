N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')
visited = [False] * N  # True: 스타트 팀, False: 링크 팀


def dfs(depth, idx):
    global min_diff

    if depth == N // 2:
        start_team = []
        link_team = []
        
        for i in range(N):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        start_score = 0
        link_score = 0

        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                start_score += S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]
                link_score += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]

        min_diff = min(min_diff, abs(start_score - link_score))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


dfs(0, 0)
print(min_diff)
