#Thembekani Gwegwana
#A module of utility functions to manipulate 2-dimensional arrays of size 4x4
#April 2014

import copy
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    return (grid)


def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+'+'-'*20+'+') #Printing out the upper part of the box
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j] == 0:
                print('{0:<5}'.format(' '),end='')
            else :
                print('{0:<5}'.format(grid[i][j]),end='')
        print('|',end='')
        print()
    print('+'+'-'*20+'+') #Printing the last part of the box


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(3):
        for j in range(3):
            if grid[i][j]== 0:
                return False
            elif grid[i][j] == grid[i][j+1]: #comparing the values next to each other
                return False
            elif grid[i][j] == grid[i+1][j]: #Comparing values below each other
                return False
    else :
        return True
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >=32: #Checks if you have won
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid = copy.deepcopy(grid) 
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2 :
        return True

    return False