"""Assignment 7 Question 2 util.py
2 May 2014 Djavan Arrigone"""

import copy #imports Python's built-in copy functions.

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append ([0] * 4)        

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    for i in grid:
        print('|',end='')
        for j in i:
            j=str(j) #Conversion from integer to string so can be be left-adjusted (5-width colums

            if j=='0':
                print(' '.ljust(5),end='')
            else:
                print(j.ljust(5),end='')
        print('|')        
        
    print('+--------------------+')

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==0: 
                return False
            elif grid[i][j]==grid[i][j+1]:
                return False
            elif grid[i][j]==grid[i+1][j]:
                return False
    else:
        return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]>=32:
                    return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    CopyGrid=copy.deepcopy(grid) #Special Python function which allows you too create new grid copy from another grid, allowing you too do so without effecting original grid.
    return CopyGrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                if grid1[i][j]==grid2[i][j]: #If condition true it will continue to search through grid. 
                    continue
                else:
                    return False
    return True
