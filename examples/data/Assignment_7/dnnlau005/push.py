"""merging functions for the 2048 game
Lauren Denny
30 April 2014"""

import util

def push_left (grid):
    """merge grid values left"""
    for row in range(4):        
        #delete 0's until none left for each row of grid
        while 0 in grid[row]:
            grid[row].remove(0)
        #complete each now smaller row with 0's at the end
        for i in range(4-len(grid[row])):
            grid[row].append(0)
        #starting on the left, if any of the first 3 numbers is equal to the number immediately to its right, replace the left-hand number with its double, delete the right-hand number and add a 0 to the end of the row
        for col in range(3):
            if grid[row][col]==grid[row][col+1]:
                grid[row][col]*=2
                del grid[row][col+1]
                grid[row].append(0) 
    #return left-merged grid
    return grid


def push_right (grid):
    """merge grid values right"""
    for row in range(4):        
        #delete 0's until none left for each row of grid
        while 0 in grid[row]:
            grid[row].remove(0)
        #complete each now smaller row with 0's at the beginning
        for i in range(4-len(grid[row])):
            grid[row].insert(0,0)
        #starting on the right, if any of the last 3 numbers is equal to the number immediately to its left, replace the right-hand number with its double, delete the left-hand number and add a 0 to the beginning of the row
        for col in range(-1,-4,-1):
            if grid[row][col]==grid[row][col-1]:
                grid[row][col]*=2
                del grid[row][col-1]
                grid[row].insert(0,0)        
    #return right-merged grid    
    return grid

def push_up (grid):
    """merge grid values upwards"""
    #create temporary 4x4 grid
    temp_grid=util.copy_grid(grid)
    #populate temp_grid with the values of grid with rows and columns swapped
    for row in range(4):
        for col in range(4):
            temp_grid[row][col]=grid[col][row]
    #merge temp_grid to the left ("to the top of grid")
    push_left(temp_grid)
    #swop columns and rows again to get upwards-merged grid
    for row in range(4):
        for col in range(4):
            grid[row][col]=temp_grid[col][row]
    #return upwards-merged grid
    return grid

def push_down (grid):
    """merge grid values downwards"""
    #create temporary 4x4 grid
    temp_grid=util.copy_grid(grid)
    
    #populate temp_grid with the values of grid with rows and columns swapped
    for row in range(4):
        for col in range(4):
            temp_grid[row][col]=grid[col][row]
    
    #merge temp_grid to the right ("to the bottom of grid")
    push_right(temp_grid)
   
    #swop columns and rows again to get downwards-merged grid
    for row in range(4):
        for col in range(4):
            grid[row][col]=temp_grid[col][row]
    
    #return downwards-merged grid
    return grid