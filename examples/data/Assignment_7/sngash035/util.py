"""Module to manipulate 2-dimensional arrays of size 4x4
Ashton Singh
30 April"""

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0,0,0,0]) 
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(len(grid)):
        print("|", end = "")
        for j in range(len(grid)):
            if (grid[i][j] == 0):
                grid[i][j] = "" 
            print ("{0: <5}".format(grid[i][j]), end = "")
            if (grid[i][j] == ""):
                grid[i][j] = 0           
        print("|", end = "")
        print()
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = True
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]: 
                lost = False

    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]: 
                lost = False    
              
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0: 
                lost = False
            
    return lost
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] >= 32: 
                won = True
    return won    


def copy_grid(grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid) 

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2: 
        return True
    else:
        return False