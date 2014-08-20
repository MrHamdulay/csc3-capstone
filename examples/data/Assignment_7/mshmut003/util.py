# A module of utility functions
# MSHMUT003
# 28 April 2104
import copy
def create_grid(grid):
    '''Create a 4x4 grid'''
    ht = 4
    grid = []
    for i in range(ht):
        grid.append([0]*4)
        return grid

def print_grid(grid):
    
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+'+'-'*(20)+'+')
    for i in range (4):
        print('|',end='')
        for j in range (4):
            if grid[i][j] == 0:
                print("{0:<5}".format(' '),end="")
            else:
                print("{0:<5}".format(grid[i][j]),end="")
        print('|')    
    print('+'+'-'*(20)+'+')
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return False
            elif grid[i][j] == grid[i][j+1]:
                return False
    #for i in range(4):
    #    for j in range(4):
     #       if grid[j][i] != 0:
      #          return True
            elif grid[i][j] == grid[i+1][j]:
                return False
    else:
            return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if int(grid[i][j]) >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    #new_grid = grid
    #return new_grid
    new_grid=copy.deepcopy(grid)
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False
            