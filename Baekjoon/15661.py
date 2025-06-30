import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')
selected = [False] * N  # 해당 인덱스를 팀1에 포함할지 여부

# 재귀로 부분집합 탐색
def dfs(idx):
    global min_diff

    if idx == N:
        team1, team2 = [], []
        
        for i in range(N):
            if selected[i]:
                team1.append(i)
            else:
                team2.append(i)

        # 두 팀이 모두 최소 1명 이상일 때만 계산
        if len(team1) == 0 or len(team2) == 0:
            return

        def calc(team):
            score = 0
            for i in team:
                for j in team:
                    score += S[i][j]
            return score

        diff = abs(calc(team1) - calc(team2))
        min_diff = min(min_diff, diff)
        return

    # idx번 사람을 팀1에 넣음
    selected[idx] = True
    dfs(idx + 1)

    # idx번 사람을 팀1에 넣지 않음 (팀2로 감)
    selected[idx] = False
    dfs(idx + 1)

dfs(0)
print(min_diff)
