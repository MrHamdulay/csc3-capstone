"""Dipanjali Samoo
SMXDIP001
Assignment 7_Question 3"""

                
def push_down (grid):
    """this will help us merge grid values downwards"""
    for i in range(3):
        for row in range(2,-1,-1):
            for column in range(3,-1,-1):
                if grid[row+1][column] == 0:
                    grid[row+1][column] = grid[row][column]
                    grid[row][column] = 0
                    
    for row in range(2,-1,-1):
        for column in range(3,-1,-1):    
                if grid[row+1][column] == grid[row][column]:
                    grid[row+1][column] = grid[row+1][column]*2
                    grid[row][column] = 0
                    
    for row in range(2,-1,-1):
        for column in range(3,-1,-1):
            if grid[row+1][column] == 0:
                grid[row+1][column] = grid[row][column]
                grid[row][column] = 0
                
    return grid
                                                          
def push_left (grid):
    """this will merge grid values left"""
    for i in range(3):
        for row in range(4):
            for column in range(1,4):
                if grid[row][column-1] == 0:
                    grid[row][column-1] = grid[row][column]
                    grid[row][column] = 0
                    
    for row in range(4):
        for column in range(1,4):                    
            if grid[row][column-1] == grid[row][column]:
                grid[row][column-1] = grid[row][column-1]*2
                grid[row][column] = 0
                
    for row in range(4):
        for column in range(1,4):
            if grid[row][column-1] == 0:
                grid[row][column-1] = grid[row][column]
                grid[row][column] = 0

    return grid

def push_up (grid):
    """this wil merge grid values upwards"""
    for i in range(3):
        for row in range(1,4):
            for column in range(4):
                if grid[row-1][column] == 0:
                    grid[row-1][column] = grid[row][column]
                    grid[row][column] = 0
                   
    for row in range(1,4):
        for column in range(4):    
                if grid[row-1][column] == grid[row][column]:
                    grid[row-1][column] = grid[row-1][column]*2
                    grid[row][column] = 0
                        
    for row in range(1,4):
        for column in range(4):
            if grid[row-1][column] == 0:
                grid[row-1][column] = grid[row][column]
                grid[row][column] = 0    
                
    return grid

def push_right (grid):
    """tis will merge grid values right"""   
    for i in range(3):
        for row in range(3,-1,-1):
            for column in range(2,-1,-1):
                if grid[row][column+1] == 0:
                    grid[row][column+1] = grid[row][column]
                    grid[row][column] = 0
                    
    for row in range(3,-1,-1):
        for column in range(2,-1,-1):
            if grid[row][column+1] == grid[row][column]:
                grid[row][column+1] = grid[row][column+1]*2
                grid[row][column] = 0
                
    for row in range(3,-1,-1):
        for column in range(2,-1,-1):
            if grid[row][column+1] == 0:
                grid[row][column+1] = grid[row][column]
                grid[row][column] = 0
                
    return grid