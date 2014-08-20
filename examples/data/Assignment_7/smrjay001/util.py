"""
Assignment 7 - Question 2
A module of utility functions used to manipulate 2D arrays of size 4x4.
Jayan Smart
29 April 2014
"""

def create_grid(grid):
    """create a 4x4 grid"""
    row = []
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box""" 
        
    print('+--------------------+')
    for i in range (len(grid)):
        print("|", end="")
        for j in range(len(grid)):
            if grid[i][j] == 0:
                print ("     ",end="")
            else:
                print(str(grid[i][j]).ljust(5), end="")
        print("|")
    print('+--------------------+')
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    ##Look for blank spaces
    for y in range (4):
        if 0 in grid[y]:
            return False
    
    ##Check through each row
    for i  in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1]:
                return False
            
    ##check through each colum
            col1=grid[j][i]
            col2=grid[j+1][i]
            if col1==col2: 
                return False
            
    return True
        

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        row = grid[i]
        for value in row:
            if value >=32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    from copy import deepcopy
    new_grid=deepcopy(grid)
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False
