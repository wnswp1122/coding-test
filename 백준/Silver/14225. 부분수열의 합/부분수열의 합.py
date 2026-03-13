import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
result = [0] + [-1 for _ in range(2000000)]
arr = []
visited = [False for _ in range(N+1)]

def dfs(start):
    check = sum(arr)
    result[check] = check

    for i in range(start, N):
        if visited[i]:
            continue

        arr.append(S[i])
        visited[i] = True
        dfs(i)
        arr.pop()
        visited[i] = False
    return

dfs(0)
print(result.index(-1))