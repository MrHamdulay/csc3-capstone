"""A list of functions to be used to move the numbers on a grid in the game 2048
by Jeremy Smith SMTJER002
1 May 2014"""

import util

def push_up (grid):
    """merges grid values upwards"""
    #moves values upwards
    old_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while util.grid_equal(grid,old_grid) == False:
        old_grid = util.copy_grid(grid)
        for row in range(3):
            for col in range(4):
                if grid[row][col] == 0 and grid[row+1][col] != 0:
                    grid[row][col] = grid[row+1][col]
                    grid[row+1][col] = 0
    #merges like values upwards    
    for row in range (3):
        for col in range(4):
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] += grid[row+1][col]
                grid[row+1][col] = 0
    #moves values upwards
    for row in range(3):
        for col in range(4):
            if grid[row][col] == 0 and grid[row+1][col] != 0:
                grid[row][col] = grid[row+1][col]
                grid[row+1][col] = 0
                
    return grid
    
def push_down (grid):
    """merges grid values downwards"""
    #moves values downwards
    old_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while util.grid_equal(grid,old_grid) == False:
        old_grid = util.copy_grid(grid)
        for row in range(3,0,-1):
            for col in range(3,-1,-1):
                if grid[row][col] == 0 and grid[row-1][col] != 0:
                    grid[row][col] = grid[row-1][col]
                    grid[row-1][col] = 0
    #merges values downwards
    for row in range (3,0,-1):
        for col in range(3,-1,-1):
            if grid[row][col] == grid[row-1][col]:
                grid[row][col] += grid[row-1][col]
                grid[row-1][col] = 0
    #moves values downwards
    for row in range(3,0,-1):
        for col in range(3,-1,-1):
            if grid[row][col] == 0 and grid[row-1][col] != 0:
                grid[row][col] = grid[row-1][col]
                grid[row-1][col] = 0
                
    return grid

def push_left (grid):
    """merges grid values left"""
    #moves values to the left
    old_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while util.grid_equal(grid,old_grid) == False:
        old_grid = util.copy_grid(grid)
        for row in range(4):
            for col in range(3):
                if grid[row][col] == 0 and grid[row][col+1] != 0:
                    grid[row][col] = grid[row][col+1]
                    grid[row][col+1] = 0
    #merges values to the left
    for row in range (4):
        for col in range(3):
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] += grid[row][col+1]
                grid[row][col+1] = 0
    #moves values to the left                  
    for row in range(4):
        for col in range(3):
            if grid[row][col] == 0 and grid[row][col+1] != 0:
                grid[row][col] = grid[row][col+1]
                grid[row][col+1] = 0
    return grid

def push_right (grid):
    """merges grid values right"""
    #moves values to the right
    old_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while util.grid_equal(grid,old_grid) == False:
        old_grid = util.copy_grid(grid)
        for row in range(3,-1,-1):
            for col in range(3,0,-1):
                if grid[row][col] == 0 and grid[row][col-1] != 0:
                    grid[row][col] = grid[row][col-1]
                    grid[row][col-1] = 0
    #merges values to the right
    for row in range (3,-1,-1):
        for col in range(3,0,-1):
            if grid[row][col] == grid[row][col-1]:
                grid[row][col] += grid[row][col-1]
                grid[row][col-1] = 0
    #moves values to the right
    for row in range(3,-1,-1):
        for col in range(3,0,-1):
            if grid[row][col] == 0 and grid[row][col-1] != 0:
                grid[row][col] = grid[row][col-1]
                grid[row][col-1] = 0    
                
    return grid