import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
grid = []
cleaner = []  

for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] == -1:
            cleaner.append(i)
    grid.append(row)

def spread(grid):
    new_grid = [row[:] for row in grid]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for x in range(R):
        for y in range(C):
            if grid[x][y] <= 0:
                continue
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != -1:
                    new_grid[nx][ny] += grid[x][y] // 5
                    cnt += 1
            new_grid[x][y] -= (grid[x][y] // 5) * cnt
    return new_grid

def rotate(grid):
    top = cleaner[0]  
    bot = cleaner[1]    

    for i in range(top - 1, 0, -1):
        grid[i][0] = grid[i-1][0]
    for i in range(0, C - 1):
        grid[0][i] = grid[0][i+1]
    for i in range(0, top):
        grid[i][C-1] = grid[i+1][C-1]
    for i in range(C - 1, 1, -1):
        grid[top][i] = grid[top][i-1]
    grid[top][1] = 0

    for i in range(bot + 1, R - 1):
        grid[i][0] = grid[i+1][0]
    for i in range(0, C - 1):
        grid[R-1][i] = grid[R-1][i+1]
    for i in range(R - 1, bot, -1):
        grid[i][C-1] = grid[i-1][C-1]
    for i in range(C - 1, 1, -1):
        grid[bot][i] = grid[bot][i-1]
    grid[bot][1] = 0

    return grid

for _ in range(T):
    grid = spread(grid)
    grid = rotate(grid)

result = sum(sum(row) for row in grid) + 2
print(result)