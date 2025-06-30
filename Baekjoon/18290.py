N, M, K =  map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
max_sum = float('-inf')

def can_select(r, c):
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc]:
                return False
    return True

def backtracking(r,c,d,s):#row, col, depth, sum
    global max_sum

    if d == K:
        max_sum = max(s, max_sum)
        return 

    if r == N:
        return 
    
    nr, nc = (r, c+1) if c+1 < M else (r+1, 0)

    backtracking(nr, nc, d, s)

    if can_select(r,c) and not visited[r][c]:
        visited[r][c] = True
        backtracking(nr,nc,d+1,s + matrix[r][c])
        visited[r][c] = False

backtracking(0,0,0,0)
print(max_sum)
        
