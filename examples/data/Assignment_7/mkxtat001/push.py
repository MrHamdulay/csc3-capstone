def push_up (grid):
    """merge grid values upwards"""
    for k in range(3):
        for row in range(3,0,-1):
            for column in range(4):            
                if grid[row-1][column] == 0:
                    grid[row-1][column] = grid[row][column]
                    grid[row][column] = 0    
    j = 0
    while j < 3:
        for i in range(4):
            if grid[j][i] == grid[j+1][i]:
                merge = grid[j][i] + grid[j+1][i]
                grid[j+1][i] = 0
                grid[j][i] = merge
        j += 1

    for k in range(3):
        for row in range(3,0,-1):
            for column in range(4):            
                if grid[row-1][column] == 0:
                    grid[row-1][column] = grid[row][column]
                    grid[row][column] = 0         
    return(grid)

def push_down(grid):
    """merge grid values downwards"""
    for k in range(3):
        for row in range(3):
            for column in range(4):
                if grid[row+1][column] == 0:
                    grid[row+1][column] = grid[row][column]
                    grid[row][column] = 0    
    j = 0
    while j < 3:
        for i in range(4):
            if grid[j][i] == grid[j+1][i]:
                merge = grid[j][i] + grid[j+1][i]
                grid[j+1][i] = 0
                grid[j][i] = merge
        j += 1

    for k in range(3):
        for row in range(3):
            for column in range(4):
                if grid[row+1][column] == 0:
                    grid[row+1][column] = grid[row][column]
                    grid[row][column] = 0  
    return(grid)

def push_left (grid):
    """merge grid values left"""
    for k in range(3):
        for row in range(4):
            for column in range(3,0,-1):
                if grid[row][column-1] == 0:
                    grid[row][column-1] = grid[row][column]
                    grid[row][column] = 0    
    j = 0
    while j < 4:
        for i in range(3):
            if grid[j][i] == grid[j][i+1]:
                merge = grid[j][i] + grid[j][i+1]
                grid[j][i+1] = 0
                grid[j][i] = merge
        j += 1

    for k in range(3):
        for row in range(4):
            for column in range(3,0,-1):
                if grid[row][column-1] == 0:
                    grid[row][column-1] = grid[row][column]
                    grid[row][column] = 0 
    return(grid)    

def push_right (grid):
    """merge grid values right""" 
    for k in range(3):
        for row in range(4):
            for column in range(3):
                if grid[row][column+1] == 0:
                    grid[row][column+1] = grid[row][column]
                    grid[row][column] = 0    
    j = 0
    while j < 4:
        for i in range(3):
            if grid[j][i] == grid[j][i+1]:
                merge = grid[j][i] + grid[j][i+1]
                grid[j][i+1] = 0
                grid[j][i] = merge
        j += 1

    for k in range(3):
        for row in range(4):
            for column in range(3):
                if grid[row][column+1] == 0:
                    grid[row][column+1] = grid[row][column]
                    grid[row][column] = 0 
    return(grid)    
