def push_up(grid):
    collum = []
    
    for k in range(3):
        for j in range(4):
            for i in range(3):
            
                if grid[i][j] == 0:
                    grid[i][j] ,grid[i+1][j] = grid[i+1][j], 0
                elif (grid[i][j] == grid[i+1][j]) and j not in collum :
                    grid[i][j] , grid[i+1][j] = grid[i+1][j] + grid[i][j], 0
                    collum.append(j)
                    
                    
    return grid


def push_right(grid):
    row = []
    
    for k in range(3):
        for i in range(4):
            for j in range(3,0,-1):
                if grid[i][j] == 0:
                    grid[i][j] ,grid[i][j-1] = grid[i][j-1], 0
                elif grid[i][j] == grid[i][j-1] and i not in row:
                    grid[i][j] , grid[i][j-1] = grid[i][j-1] + grid[i][j], 0
                    row.append(i)
    return grid

def push_down(grid):
    collum = []
    for k in range(3):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i][j] == 0:
                    grid[i][j] ,grid[i-1][j] = grid[i-1][j], 0
                elif grid[i][j] == grid[i-1][j] and j not in collum:
                    grid[i][j] , grid[i-1][j] = grid[i-1][j] + grid[i][j], 0
                    collum.append(j)
    return grid


def push_left(grid):
    row = []
    for k in range(3):
        for i in range(4):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] ,grid[i][j+1] = grid[i][j+1], 0
                elif grid[i][j] == grid[i][j+1] and i not in row :
                    grid[i][j] , grid[i][j+1] = grid[i][j+1] + grid[i][j], 0
                    row.append(i)
    return grid

                
                