"""Assignment 7, question 3
JT
01-05-2014"""

def push_up (grid):
    """merge grid values upwards"""
    #print(grid)
    for x in range(4):
        j = 0
        while j < 4:
            for i in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i + 1][j]
                    grid[i+1][j] = 0
            j += 1 
    j = 0
    while j < 4:
        for i in range(3):    
            if grid[i][j] == grid[i+1][j]:
                grid[i][j] = grid[i][j] + grid[i+1][j]
                grid[i+1][j] = 0 
        j += 1
    for x in range(4):
        j = 0
        while j < 4:
            for i in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i + 1][j]
                    grid[i+1][j] = 0
            j += 1     
    return grid

def push_down (grid):
    """merge grid values downwards"""
    #print(grid)
    for x in range(4):
        j = 0
        while j < 4:
            for i in range(3,0,-1):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i-1][j]
                    grid[i-1][j] = 0                    
            j += 1
    j = 0
    while j < 4:
        for i in range(3,0,-1):
            if grid[i][j] == grid[i-1][j]:
                grid[i][j] = grid[i][j] + grid[i-1][j]
                grid[i-1][j] = 0
        j += 1
    for x in range(4):
        j = 0
        while j < 4:
            for i in range(3,0,-1):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i-1][j]
                    grid[i-1][j] = 0                    
            j += 1    
    #print(grid)    
    return grid    


def push_left (grid):
    """merge grid values left"""
    for x in range(4):
        for i in range(4):
            j = 0
            while j < 3:
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0
                j += 1
    j = 0
    for i in range(4):
        while j < 3:
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] = grid[i][j] + grid[i][j+1]
                grid[i][j+1] = 0 
            j += 1
    for x in range(4):
        for i in range(4):
            j = 0
            while j < 3:
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0
                j += 1    
    #print(grid)
    return grid
            

def push_right (grid):
    """merge grid values right"""  
    for x in range(4):
            for i in range(4):
                j = 3
                while j > 0:
                    if grid[i][j] == 0:
                        grid[i][j] = grid[i][j-1]
                        grid[i][j-1] = 0
                    j -= 1
    j = 4
    for i in range(4):
        while j > 0:
            j -= 1
            if grid[i][j] == grid[i][j-1]:
                #print(grid[i][j])
                grid[i][j] = grid[i][j] + grid[i][j-1]
                grid[i][j-1] = 0    
            #j -= 1
    for x in range(4):
            for i in range(4):
                j = 3
                while j > 0:
                    if grid[i][j] == 0:
                        grid[i][j] = grid[i][j-1]
                        grid[i][j-1] = 0
                    j -= 1    
    #print(grid)
    return grid    
          