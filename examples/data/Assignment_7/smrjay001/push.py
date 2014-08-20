"""
Assignment 7 - Question 3
Module of functions that control user imput in the 2048 game.
Jayan Smart
01 May 2014
"""
def push_up (grid):
    """merge grid values upwards"""
    for i in range (3):
        for row in range(1,4):
            for col in range(4):
                if grid[row-1][col] == 0:
                    grid[row-1][col] = grid[row][col]
                    grid[row][col] = 0
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] = grid[row-1][col]*2
                grid[row][col]=0
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == 0:
                grid[row-1][col] = grid[row][col]
                grid[row][col] = 0
                
    return grid
    

def push_down (grid):
    """merge grid values downwards"""
    for i in range (3):
        for row in range(2,-1, -1):
            for col in range(4):
                if grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0     
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] = grid[row-1][col]*2
                grid[row][col]=0                
    for i in range (3):
        for row in range(2,-1, -1):
            for col in range(4):
                if grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0  
    return grid
def push_left (grid):
    """merge grid values left"""
    
    for i in range(4):
        row = grid[i]
        
        if row == [0, 0 ,0 ,0]:
            continue
        for k in range(4):
            for j in range(1, 4):
                if row[j-1] == 0:
                    row[j-1] = row[j]
                    row[j] = 0
        for l in range(1, 4):
            if row[l-1] == row[l]:
                row[l-1] = row[l]*2
                row[l] = 0
        for j in range(1, 4):
            if row[j-1] == 0:
                row[j-1] = row[j]
                row[j] = 0                
        grid[i] = row
    return grid
                
                

def push_right (grid):
    """merge grid values right"""
    for i in range(4):
        row = grid[i]
        
        if row == [0, 0 ,0 ,0]:
            continue
        for k in range(4):
            for j in range(2 ,-1, -1):
                if row[j+1] == 0:
                    row[j+1] = row[j]
                    row[j] = 0
        for l in range(2 ,-1, -1):
            if row[l+1] == row[l]:
                row[l+1] = row[l]*2
                row[l] = 0
        for j in range(2 ,-1, -1):
            if row[j+1] == 0:
                row[j+1] = row[j]
                row[j] = 0                
        grid[i] = row
    return grid    
