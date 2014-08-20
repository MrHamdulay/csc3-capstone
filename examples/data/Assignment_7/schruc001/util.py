'''utility program
Ruchaan Schmidt
April 2014'''
                                                                   
def create_grid(grid):                                                  
    
    """create a 4x4 grid"""

    for i in range(4):                                                          # i= x-axis , j = y-axis
        grid.append([0]*4)                                                      # multiply list (same as g=[0]; g*4) (hussein used 0s for input test, 0s will be changed later)
    

def print_grid (grid):                                                          # use format for 5 width columns
    
    """print out a 4x4 grid in 5-width columns within a box"""
    
    print('+--------------------+')                                             # top line (20*-  2*+)
    for i in range(4):
        print('{0:<0}'.format('|'),end='')                                      # left align grid for bars
        for j in range(4):
            if grid[i][j]==0:                                                   # substitute 0s for empty string (look at assignment)
                print('{0:<5}'.format(''),end='')
            else:
                print('{0:<5}'.format(grid[i][j]), end ='')
        print('{0:<5}'.format('|'), end='')
        print()
    print('+--------------------+')                                             # bottom line (same as top)


def check_lost (grid):
    
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:                                                 # return false for all empty spaces
                return False
    for i in range (3,0,-1):
        for j in range(4):
            if grid[i][j] == grid[i-1][j]:                                      # equals can be merged
                return False
    for i in range(4):
        for j in range(3,0,-1):
            if grid[i][j] == grid[i][j-1]:
                return False
    else:
        return True


def check_won (grid):

    """return True if a value>=32 is found in the grid; otherwise False"""

    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:                                                # only has to be 32
                return True
    else:
        return False

import copy                                                                     # for deepcpy
def copy_grid (grid):
    
    """return a copy of the grid"""

    copy_grid = copy.deepcopy(grid)
    return copy_grid



def grid_equal (grid1, grid2):
    
    """check if 2 grids are equal - return boolean value"""
    
    if grid1 == grid2:
        return True
    else:
        return False    