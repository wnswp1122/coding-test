def dfs():
    if len(path) == N: print(' '.join(map(str, path)))

    for i in range(N):
        if not used[i]:
            used[i] = True
            path.append(arr[i])  # path에 추가
            dfs()
            path.pop()           # path에서 제거 (백트래킹)
            used[i] = False

N = int(input())
arr = list(range(1,N+1))
used = [False] * N
path = []
dfs()