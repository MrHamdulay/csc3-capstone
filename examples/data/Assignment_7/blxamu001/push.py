def push_up(grid):
    for i in range(4):
        for j in range(4):
            if grid[i-3][j] != 0 and grid[i-2][j]==0:
                grid[i-2][j] = grid[i-3][j]
                grid[i-3][j] = 0
                
            elif grid[i-2][j] != 0 and grid[i-1][j]==0:
                grid[i-1][j] = grid[i-2][j]
                grid[i-2][j] = 0
                grid[i][j] = grid[i-1][j]
            elif grid[i-1][j] != 0 and grid[i][j]==0:
                grid[i-1][j] = 0

            if grid[i-3][j+1] != 0 and grid[i-2][j+1]==0:
                grid[i-2][j+1] = grid[i-3][j+1]
                grid[i-3][j+1] = 0
            elif grid[i-2][j+1] != 0 and grid[i-1][j+1]==0:
                grid[i-1][j+1] = grid[i-2][j+1]
                grid[i-2][j+1] = 0
                grid[i][j+1] = grid[i-1][j+1]
            elif grid[i-1][j+1] != 0 and grid[i][j+1]==0:
                grid[i-1][j+1] = 0           