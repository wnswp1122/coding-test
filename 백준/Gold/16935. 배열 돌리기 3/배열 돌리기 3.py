import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ops = list(map(int, input().split()))

for op in ops:

    if op == 1:  
        arr = arr[::-1]

    elif op == 2: 
        arr = [row[::-1] for row in arr]

    elif op == 3:  
        arr = [list(row) for row in zip(*arr[::-1])]
        N, M = M, N

    elif op == 4: 
        arr = [list(row) for row in zip(*arr)][::-1]
        N, M = M, N

    elif op == 5:  
        new = [[0]*M for _ in range(N)]
        n, m = N//2, M//2

        for i in range(n):
            for j in range(m):
                new[i][j+m] = arr[i][j]

        for i in range(n):
            for j in range(m, M):
                new[i+n][j] = arr[i][j]

        for i in range(n, N):
            for j in range(m, M):
                new[i][j-m] = arr[i][j]

        for i in range(n, N):
            for j in range(m):
                new[i-n][j] = arr[i][j]

        arr = new

    elif op == 6:
        new = [[0]*M for _ in range(N)]
        n, m = N//2, M//2

        for i in range(n):
            for j in range(m):
                new[i+n][j] = arr[i][j]

        for i in range(n, N):
            for j in range(m):
                new[i][j+m] = arr[i][j]

        for i in range(n, N):
            for j in range(m, M):
                new[i-n][j] = arr[i][j]

        for i in range(n):
            for j in range(m, M):
                new[i][j-m] = arr[i][j]

        arr = new

for row in arr:
    print(*row)