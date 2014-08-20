'''module of utility functions to manipulate 2-dimensional 4x4 arrays
nasreen hoosain
30 april 2014'''

import copy

def create_grid(grid):
    '''create a 4x4 grid'''
    g = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    for l in g:
        grid.append(l)    
    return grid

def print_grid(grid):
    '''print out a 4x4 grid in 5-width columns within a box'''
    a = '+--------------------+'
    form = '{0:<5}' #format for columns
    print(a)
    for col in range(4):
        print('|', end = '')
        for row in range(4):
            if grid[col][row] == 0:
                print(form.format(''), end = '') #if zero, print empty string
            else:
                print(form.format(grid[col][row]), end = '')
        print('|')
    print(a)
    
def check_lost(grid):
    '''return True if there are no 0 values and no adjacent values that are equal; otherwise False'''
    for col in range(4):
        for row in range(4):
            if grid[col][row] == 0: #if there is a zero in grid
                return False
            if (row-1) != -1: #make sure there is a row above
                if grid[col][row] == grid[col][row-1]:
                    return False
            if (row+1) != 4: #make sure there is a row below
                if grid[col][row] == grid[col][row+1]: 
                    return False
            if (col-1) != -1: #make sure there is a column to the left
                if grid[col][row] == grid[col-1][row]:
                    return False
            if (col+1) != 4: #make sure there is a column to the right
                if grid[col][row] == grid[col+1][row]:
                    return False
    else:
        return True
        
def check_won(grid):
    '''return True if a value >= 32 is found in the grid; otherwise False'''
    for col in range(4):
        for row in range(4):
            if 32 <= grid[col][row]:
                return True
    else:
        return False        
    
def copy_grid(grid):
    '''return a copy of the grid'''
    grid_copy = copy.deepcopy(grid) #uses in-built deepcopy function to copy grid
    return grid_copy

def grid_equal(grid1, grid2):
    '''check if 2 grids are equal - return boolean value'''
    for col in range(4):
        for row in range(4):
            if grid1[col][row] != grid2[col][row]: #if a difference is found, return false
                return False
    else:
        return True #if no difference is found