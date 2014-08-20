'''Module contaning functions used to play 2048
Nkosi Gumede
30 April 2014'''

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for a in range(4):
        grid.append([0,0,0,0])
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    times=4
    column=5
    print('+'+'-'*times*column+'+')
    for row in range(4):        
        print("|",end="")
        for col in range(4):
            if grid[row][col]==0:
                grid[row][col]=" "
                print("{0:<5}".format(grid[row][col]),end="")
            else:
                print("{0:<5}".format(grid[row][col]),end="")
        print("|")
    print('+'+'-'*times*column+'+')
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0:
                return False
    for row in range(4):
        for col in range(4):
            specific_grid=grid[row][col]
            if 0<=col+1<4:
                if specific_grid==grid[row][col+1]:
                    return False
            if 0<col-1<4:
                if specific_grid==grid[row][col-1]:
                    return False
            if 0<=row+1<4:
                if specific_grid==grid[row+1][col]:
                    return False
            if 0<row-1<4:
                if specific_grid==grid[row-1][col]:
                    return False
        
    return True
            
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return True
    return False
    
def copy_grid (grid):
    """return a copy of the grid"""
    
    copied=copy.deepcopy(grid)
    return copied
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    global copy
    global grid
    copy= grid1
    grid= grid2
    if copy ==grid:
        return True
    else:
        return False