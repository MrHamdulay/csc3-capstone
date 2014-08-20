''' Assignment 7, question 2
This is a module of utility functions to manipulate 2D arrays of size 4x4
Tristan Subroyen
28 April 2014 '''

import copy

def create_grid (grid):
    ''' create a 4x4 grid '''
    # iterate for value 4
    for i in range (4):
        grid.append([0]*4) # add items to the grid

def print_grid (grid):
    ''' print out a 4x4 grid in 5-width columns within a box '''
    
    print("+--------------------+")
    # iterate through the grid:
    for i in range (4):
        for j in range (4):
            if j == 0: # if at the left boundary, print the border    
                print("|",end="")
            if grid[i][j] == 0:
                grid[i][j] = ''
            print("{0:<5}".format(grid[i][j]),end='',sep='') # print the values, formatted
            if j == 3:
                print("|",end="") # if at the right border, print the border
        print() # leave a line for display purposes
    print("+--------------------+")

def check_lost (grid):
    ''' return True if there are no 0 values and no adjacent values that are equal; otherwise False '''
    # test values
    noZero = 0
    noAdj = 0
    
    # check if any zero values are present:                
    for i in range (4):
        for j in range (4):
            if grid[i][j] == '':
                grid[i][j] = 0
            if grid[i][j] == 0:
                noZero += 1
    
    # check if any adjacent values are present:
    for i in range (4):
        for j in range (4):
            if grid[i][j] == '':
                grid[i][j] = 0    
    for i in range (1,2):
        for j in range (1,2):
            if (grid[i][j] == grid[i+1][j]) or (grid[i][j] == grid[i][j+1]):
                noAdj += 1
    # return appropriate boolean value
    if (noAdj == 0) and (noZero == 0):
        return True
    else:
        return False          

def check_won (grid):
    ''' return True if a value>=32 is found in the grid; otherwise False '''
    check = 0 # this value is used to keep track of values >= 32
    # iterate through the grid:
    for i in range (4):
        for j in range (4):
            if grid[i][j] == '':
                grid[i][j] = 0
                
    for i in range (4):
        for j in range (4):
            if int(grid[i][j]) >= 32: # if a grid value is >= 32
                check = check+1 # increase check
            else:
                check += 0 # do nothing with check
                
    # check if check has recorded a value >= 32            
    if check > 0:
        return True
    else:
        return False
    
def copy_grid(grid):
    ''' return a copy of the grid '''
    for i in range (4):
        for j in range (4):
            if grid[i][j] == '':
                grid[i][j] = 0    
    grid2 = copy.deepcopy(grid) # use deepcopy function to copy grid
    return grid2

def grid_equal (grid1, grid2):
    ''' check if 2 grids are equal - return boolean value '''
    for i in range (4):
        for j in range (4):
            if grid1[i][j] == '':
                grid1[i][j] = 0    
    checkEq = 0 # value used to store number of equal values
    for i in range (4):
        for j in range (4):
            if grid1[i][j] == grid2[i][j]:
                checkEq +=1 # if 2 corresponding values are equal, add one to checkEq
    if checkEq == 16: # if 2 grids are identical, checkEq should be 16
        return True
    else:
        return False
    
